import processing.serial.*;
import grafica.*;
import cc.arduino.*;
import java.lang.Math;
import java.lang.Exception;

import javax.swing.*;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;


/**
* Exception class to recognize measurements with too high deviation and handle them
* accordingly.
*/
class DeviationException extends Exception {
  
  /**
  * Creates a DeviationException with a threshold and a sigma over said threshold.
  */
  DeviationException(double threshold, double sigma){
    super("Deviation over the threshold (deviation: "+sigma+", threshold: "+threshold);
  }
}
Arduino arduino;
//Define all importan variable: which pin measures voltIn, which is the light pin,etc
int startPin = 6;
int inputPin = 7;
int lightPin = 2;
int ammountPerMeasurement = 50; //Sample number to calculate the average of a data point.
int numberofMeasurements = 12;
int delayPerMeasurement = 50; //Delay between each data point.
int delayOn = 30000; //Time in ms that the light should stayed turn on before starting to measure.
int delayOff = 500; //Time in ms that should be wait BEFORE turning off the light after a measurement is completed.
int delaybetweenMeasurements = 299500;
int katzi = 1500000; //Katzi's constant
double gamma = 0.8;
double matthias = 3.7584; //Matthia's constant
double matthiasDeviation = 0.133;


Measurement voltIn; //Null value for for the voltage divider.
boolean sick = false;
boolean measureDone = false;
double thresholdReaction = 4;

String filePath = "D:\\Documentos\\IGEM\\Lightbringer_GUI\\Data\\20171021_finalversion.txt"; //Folder of the results file
/**
* Class to facilitate the measurement of each entry.
*/
class Measurement{
  int[] list = new int[ammountPerMeasurement];
  double average = 0;
  double deviation = 0;
  int measuredPin;
  double resistance = -3215; //TODO: CHANGE THIS.
  double deviationResistance;
  double concentration;
  double deviationConcentration;
  
  /**
  * Creates and binds the Measurement to a certain pin. Measures each entry and calculates the 
  * average and deviation.
  */
  public Measurement(int pin){
    this.measuredPin = pin;
    refreshMeasurement();
  }
  
  public double getResistance(){
    return this.resistance;
  }
  
  public double getResistanceDeviation(){
    return this.deviationResistance;
  }
  
  public void setConcentration(double concentration){
    this.concentration = concentration;
  }
  
  public double getConcentration(){
    return this.concentration;
  }
  
  
  /**
  * Saves all the analogReads in the list array. After saving a single entry,
  * the programs halts for delayPerMeasurement ms.
  */
  private void measureEntries(){
    for(int i = 0; i < ammountPerMeasurement; i++){
      this.list[i] = arduino.analogRead(this.measuredPin);
      delay(delayPerMeasurement);
    }
  }
  
  /**
  *Refreshes list by saving new analogReads and immediately calculates the average and deviation
  * of this new data.
  */
  private void refreshMeasurement(){
    measureEntries();
    calculateAverage();
    calculateDeviation();
  }
  
  /**
  * Calculates the average of the measurement based on its list array.
  */
  private void calculateAverage(){
    for(int value : this.list){
      average += value;
    }
    average /= this.list.length;
  }
  
  /**
  * Calcualtes the deviation of the average.
  */
  private void calculateDeviation(){
    for(int value : this.list){
      deviation += (average - value)*(average - value);
    }
    deviation = Math.sqrt(deviation)/(average * Math.sqrt(this.list.length*this.list.length-1));
  }
  /**
  * Calculates the resistance using the voltage dividr in the hardware with voltIn as null value.
  */
  private void calculateResistance(Measurement voltIn){
   this.resistance = katzi/(voltIn.average/this.average -1);
  }
  
  /**
  * Calculates the deviation of the resistance.
  * @param voltIn null value in the voltage divider.
  */
  private void calculateDeviationResistance(Measurement voltIn){
    double deviationIn2 = voltIn.deviation * voltIn.deviation;
    double deviationOut2 = this.deviation * this.deviation;
    deviationResistance = (this.resistance/katzi) * (voltIn.average/this.average)*(Math.sqrt(deviationIn2 + deviationOut2)+1/voltIn.average+1/this.average);
  }
  
  /**
  * Calculates the fluorescin concentration using another measurement as blank.
  * @param blank , assumed to have a fluorescin concentration of 0.
  */
  private void calculateConcentration(Measurement blank){
    this.concentration = (float) (Math.pow(blank.getResistance()/this.resistance,1/(gamma))-1)/matthias;
  }
  
  /**
  * Calculates the deviation of the concentration
  * @param blank , assumed to have a fluorescin concentration of 0.
  */
  private void calculateConcentrationDeviation(Measurement blank){
    this.deviationConcentration = Math.sqrt(Math.pow(blank.getResistance()/this.resistance,2/gamma)*(1/matthias*matthias*this.concentration*this.concentration)*(blank.getResistanceDeviation()*blank.getResistanceDeviation()+this.getResistanceDeviation()*this.getResistanceDeviation())+matthiasDeviation*matthiasDeviation);
  }
  
  
 /**
  * Validates the measurement by checking if the deviation is over a certain threshold.
  * If that is not met, the function refreshes the measurement and checks again. This is
  * repeated up to tries-1 times. If the deviation is still over the threshold an exception is thrown.
  * @param threshold maximal value that the deviation can have to be accepted
  * @param tries number of times the set of analogReads should be repeated before considing the measurement a fail.
  * @throws DeviationException if after repeating the filling of the list tries-times, the deviation is still over the threshold.
  */
  private void validateMeasurement(double threshold, int tries) throws DeviationException{
    int currentTry = 0;
    try{
      if(this.deviation > threshold){
        throw new DeviationException(threshold,this.deviation);
      }
    } catch (DeviationException e){
      currentTry++;
      if(currentTry <= tries){
        this.refreshMeasurement();
        validateMeasurement(threshold, tries-1);
      } else {
        throw e;
      }
    }
  }
  
   /**
  * To string. For console printing
  */
  public String toString(){
    String temp = "Average: " + average +"\r\n";
    temp += "Deviation: " + deviation + "\r\n";
    //if(this.resistance != -3215){
      temp += "Resistance: "+this.resistance + "\r\n";
      temp += "Deviation Resistance: "+this.deviationResistance + "\r\n";
    //}
    for(int i = 0; i < this.list.length; i++){
      temp += i+": "+this.list[i]+"\n";
    }
    return temp+"\r\n \r\n";  //For .txt output
  }
  
  
  /**
  * Creates a row for .csv as a string with all attributes of the measurement.
  */
  public String mytoString(){
      String temp = "";
      for(int i = 0; i < this.list.length; i++){
        temp += this.list[i]+",";
      }
      temp += average+",";
      temp += deviation+",";
      temp += resistance+",";
      temp += deviationResistance+","; 
      temp += concentration+",";
      temp += deviationConcentration+"\r\n"; 
      return temp;
  } 
}

Measurement blank;

//Defining all PImages and values relevant for the GUI.
PImage treeCascaidPNG;
PImage onPNG;
PImage offPNG;
PImage measurePNG;
PImage measurePressedPNG;
PImage loading_00PNG;
PImage loading_25PNG;
PImage loading_50PNG;
PImage loading_75PNG;
PImage loading_100PNG;
PImage firstClickPNG;
PImage secondClickPNG;
PImage measureMessagePNG;
PImage dialogPNG;
PImage buttonPowerPNG;
PImage buttonMeasurePNG;
PImage positivPNG;
PImage negativPNG;
float resizingFactor = 0.66;
GPlot plot;

//Defining the position of the elements of the GUI.
int topYdialog;
int rightXdialog;
int topYbuttonPower;
int leftXbuttonPower;
int topYbuttonMeasure;
int leftXbuttonMeasure;


boolean on = false;
int step = 0;
PImage[] loadingArrayPNG;


void setup(){
  frameRate(60);
  size(500,420);
  background(255);
  
  treeCascaidPNG = loadImage("D:\\Documentos\\IGEM\\Lightbringer_GUI\\PNG\\ON_OFF_1.png");
  onPNG = loadImage("D:\\Documentos\\IGEM\\Lightbringer_GUI\\PNG\\Power_on.png");
  offPNG = loadImage("D:\\Documentos\\IGEM\\Lightbringer_GUI\\PNG\\Power_off.png");
  measurePNG = loadImage("D:\\Documentos\\IGEM\\Lightbringer_GUI\\PNG\\Measure_off.png");
  measurePressedPNG = loadImage("D:\\Documentos\\IGEM\\Lightbringer_GUI\\PNG\\Measure_on.png");
  positivPNG = loadImage("D:\\Documentos\\IGEM\\Lightbringer_GUI\\PNG\\Positive.png");
  negativPNG = loadImage("D:\\Documentos\\IGEM\\Lightbringer_GUI\\PNG\\Negative.png");
  firstClickPNG = loadImage("D:\\Documentos\\IGEM\\Lightbringer_GUI\\PNG\\Click_1.png");
  secondClickPNG = loadImage("D:\\Documentos\\IGEM\\Lightbringer_GUI\\PNG\\Click_2.png");
  measureMessagePNG = loadImage("D:\\Documentos\\IGEM\\Lightbringer_GUI\\PNG\\Measure_1.png");
  loadingArrayPNG = new PImage[4];
  loadingArrayPNG[0] = loadImage("D:\\Documentos\\IGEM\\Lightbringer_GUI\\PNG\\Loading_025.png");
  loadingArrayPNG[1] = loadImage("D:\\Documentos\\IGEM\\Lightbringer_GUI\\PNG\\Loading_05.png");
  loadingArrayPNG[2] = loadImage("D:\\Documentos\\IGEM\\Lightbringer_GUI\\PNG\\Loading_075.png");
  loadingArrayPNG[3] = loadImage("D:\\Documentos\\IGEM\\Lightbringer_GUI\\PNG\\Loading_10.png");
  
  
  dialogPNG = treeCascaidPNG;
  buttonPowerPNG = offPNG;
  buttonMeasurePNG = measurePNG;
  
  topYdialog = (int) ((height-dialogPNG.height)/2);
  rightXdialog = (int) ((width*0.55-dialogPNG.width)/2);
  image(dialogPNG,rightXdialog,topYdialog);
  topYbuttonPower = (int) (topYdialog+dialogPNG.height-buttonPowerPNG.height*resizingFactor);
  leftXbuttonPower = (int) (width*0.58);
  image(buttonPowerPNG,leftXbuttonPower,topYbuttonPower,buttonPowerPNG.width*resizingFactor,buttonPowerPNG.height*resizingFactor);
  topYbuttonMeasure = topYdialog;
  leftXbuttonMeasure = leftXbuttonPower;
  image(buttonMeasurePNG,leftXbuttonMeasure,topYbuttonMeasure,buttonMeasurePNG.width*resizingFactor,buttonPowerPNG.height*resizingFactor);
  
}

int currentFrame = 0;
boolean showGraph = false;
boolean blankDone = false;
boolean threading = false;

int progressNumber = 0; //Meant to be used to check how far the measure is done.

void draw(){
  if(on){
    if(currentFrame == 0){
      System.out.println("progressNumber"+progressNumber);
      if(progressNumber == 0 && !threading){
        swapDialogPicture(firstClickPNG,measureMessagePNG);
      } else if(progressNumber == 1 && !threading){
        swapDialogPicture(secondClickPNG,measureMessagePNG);
      } else if(measureDone){
        if(sick) dialogPNG = positivPNG; else dialogPNG = negativPNG; //Not a beutiful solution, but a working one.
        if(!showGraph)image(dialogPNG,rightXdialog,topYdialog);
      } else if(threading){
        changeLoadingPicture(step);
        step = (step + 1) % 4;
      }
    }
    currentFrame = (currentFrame + 1) % 60;
  }
}

boolean firstPictureCurrent = true;
void swapDialogPicture(PImage first, PImage second){
  background(255);
  image(buttonPowerPNG,leftXbuttonPower,topYbuttonPower,buttonPowerPNG.width*resizingFactor,buttonPowerPNG.height*resizingFactor);
  image(buttonMeasurePNG,leftXbuttonMeasure,topYbuttonMeasure,buttonMeasurePNG.width*resizingFactor,buttonPowerPNG.height*resizingFactor);
  if(firstPictureCurrent) dialogPNG = second; else dialogPNG = first;
  firstPictureCurrent = !firstPictureCurrent;
  image(dialogPNG,rightXdialog,topYdialog);
}


/**
* Changes the picture in the loadingArrayPNG array based on the step. Only changes the current dialog picture
* if the programs hasn't finished measurring.
* @param step picture in the array that should be displayed
*/
void changeLoadingPicture(int step){
  background(255);
  image(buttonPowerPNG,leftXbuttonPower,topYbuttonPower,buttonPowerPNG.width*resizingFactor,buttonPowerPNG.height*resizingFactor);
  image(buttonMeasurePNG,leftXbuttonMeasure,topYbuttonMeasure,buttonMeasurePNG.width*resizingFactor,buttonPowerPNG.height*resizingFactor);
  if(!measureDone) dialogPNG = loadingArrayPNG[step];
  image(dialogPNG,rightXdialog,topYdialog);
}

boolean isMouseonPowerButton(){
  if(mouseX >= width*0.58 && mouseX <= width*0.58 + buttonPowerPNG.width*resizingFactor){
    if(mouseY >= topYbuttonPower && mouseY <= topYbuttonPower + buttonPowerPNG.height*resizingFactor){
      return true;
    }
  }
  return false;
}

boolean isMouseonMeasureButton(){
  if(mouseX >= width*0.58 && mouseX <= width*0.58 + buttonMeasurePNG.width*resizingFactor){
    if(mouseY >= topYbuttonMeasure && mouseY <= topYbuttonMeasure + buttonMeasurePNG.height*resizingFactor){
      return true;
    }
  }
  return false;
}
//Adds one to progressNumber respecting the range (mod operation).
void progressStep(){
  progressNumber = (progressNumber + 1) % 3;
}

void mousePressed(){
  if(isMouseonMeasureButton()){
    background(255);
    image(dialogPNG,rightXdialog,topYdialog);
    image(buttonPowerPNG,leftXbuttonPower,topYbuttonPower,buttonPowerPNG.width*resizingFactor,buttonPowerPNG.height*resizingFactor);
    buttonMeasurePNG = measurePressedPNG;
    image(buttonMeasurePNG,leftXbuttonMeasure,topYbuttonMeasure,buttonMeasurePNG.width*resizingFactor,buttonPowerPNG.height*resizingFactor);
  }
}

void mouseReleased(){
    background(255);
    image(dialogPNG,rightXdialog,topYdialog);
    image(buttonPowerPNG,leftXbuttonPower,topYbuttonPower,buttonPowerPNG.width*resizingFactor,buttonPowerPNG.height*resizingFactor);
    buttonMeasurePNG = measurePNG;
    image(buttonMeasurePNG,leftXbuttonMeasure,topYbuttonMeasure,buttonMeasurePNG.width*resizingFactor,buttonPowerPNG.height*resizingFactor);
}

void mouseClicked(){
  if(isMouseonPowerButton() && !measureDone){
    buttonPowerPNG = onPNG;
    image(dialogPNG,rightXdialog,topYdialog);
    onOff();
  }
  if(on){
    if(isMouseonMeasureButton()){
      if(progressNumber == 0 && !threading){
        thread("measureblank");
      } else if(progressNumber == 1 && !threading){
        thread("measure");
      } else if(progressNumber == 2 && !threading){
        plot.defaultDraw();
        showGraph = true;
      }
    }
  }
}

void onOff(){
  if(on){
    currentFrame = 0;
    step = 0;
    progressNumber = 0;
    dialogPNG = treeCascaidPNG;
    background(255);
    image(dialogPNG,rightXdialog,topYdialog);
    buttonPowerPNG = offPNG;
    buttonMeasurePNG = measurePNG;
    image(buttonPowerPNG,leftXbuttonPower,topYbuttonPower,buttonPowerPNG.width*resizingFactor,buttonPowerPNG.height*resizingFactor);
    image(buttonMeasurePNG,leftXbuttonMeasure,topYbuttonMeasure,buttonMeasurePNG.width*resizingFactor,buttonPowerPNG.height*resizingFactor);
  } else{
    thread("initArduino");
  }
  on = !on;
  
}

void initArduino(){
  threading = true;
  arduino = new Arduino(this,arduino.list()[0], 57600);
  arduino.pinMode(lightPin,Arduino.OUTPUT);
  delay(2000);
  System.out.println("Arduino set up propertly");
  voltIn = new Measurement(startPin);
  try{voltIn.validateMeasurement(0.3,5);}
  catch (DeviationException e){
    e.printStackTrace();
  }
  System.out.println("voltIn calculated propertly");
  threading = false;
}

void measureblank(){
  threading = true;
  blank = measurementCycle(0.3);
  threading = false;
  progressStep();
  System.out.println("measureblank done");
}

void measure(){
  threading = true;
  Measurement[] measurementsList = new Measurement[numberofMeasurements];
  try{
    BufferedWriter buff = new BufferedWriter(new FileWriter(filePath,true));
    buff.write("Measurment#,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,Average,Deviation,Resistance,ResistanceDeviation,Concentration,ConcentrationDeviation\r\n");
    buff.close(); //For .csv output
    for(int i = 0; i < measurementsList.length; i++){
    measurementsList[i] = measurementCycle(0.3,blank);
    writeMeasurement(filePath,measurementsList[i],i);
    System.out.println("Measurement number"+i+"\n"+measurementsList[i]+"\n\n");
    delay(delaybetweenMeasurements);
    }
  } catch (IOException e){
    e.printStackTrace();
  }
  for(int i = measurementsList.length-1; i > measurementsList.length-3; i--){
    if(measurementsList[i].concentration > thresholdReaction ){
      sick = true;
    }
  }
  for(int i = 0; i < 0; i++){
    sick = sick && (measurementsList[i+1].concentration > measurementsList[i].concentration);
  }
  if(sick){
    dialogPNG = positivPNG;
  } else {
    dialogPNG = negativPNG;
  }
  measureDone = true;
  threading = false;
  progressStep();
  plot = drawGraph(filePath);
  
}

/**
*This function defines what measure-cycle is composed of. For non-blank measuremetns.
*So:
*  1. Light gets turn on.
*  2. Some time is waited (delayON).
*  3. The measurement is taken.
*  4. Some time is waited (delayOff).
*  5. Light is turn off.
*  6. The measurement is validated. If invalid, measurement.list is set to null.
*  7. The measurement is returned.
* @param sigma threshold of the deviation
* @param blank measurement the current measurement should be compared to
* @returns measuremet with all attributes calculated using blank as a blank measurement. 
*/
Measurement measurementCycle(double sigma,Measurement blank){
  System.out.println("adios");
  Measurement temp = measurementCycle(sigma);
  System.out.println("uno"+temp.getConcentration());
  temp.calculateConcentration(blank);
  temp.calculateConcentrationDeviation(blank);
  System.out.println("dos"+temp.getConcentration());
  return temp;
}

/**
*This function defines what measure-cycle is composed of. For the blank measurement.
*So:
*  1. Light gets turn on.
*  2. Some time is waited (delayON).
*  3. The measurement is taken.
*  4. Some time is waited (delayOff).
*  5. Light is turn off.
*  6. The measurement is validated. If invalid, measurement.list is set to null.
*  7. The measurement is returned.
* @param sigma threshold of the deviation
* @return a blank measurement containing all relevant information.
*/
Measurement measurementCycle(double sigma){
  arduino.digitalWrite(lightPin, Arduino.HIGH);
  delay(delayOn);
  Measurement temp = new Measurement(inputPin);
  delay(delayOff);
  arduino.digitalWrite(lightPin,Arduino.LOW);
  try{
    temp.validateMeasurement(sigma,1);
    if(voltIn != null){
      temp.calculateResistance(voltIn);
      temp.calculateDeviationResistance(voltIn);
      temp.setConcentration(0);
    }
  } catch (DeviationException e){
    temp.list = null;
  }
  return temp;
}

/**
* Writes a measurement to the specified filePath and binds it to number.
* @param filePath location of the file where the measurement should be written to.
* @param measurement measurement to be printed as String.
* @param measurementnumber number to be added before the measurement String.
*/
void writeMeasurement(String filePath, Measurement measurement, int measurementnumber) throws IOException{
  BufferedWriter buff = new BufferedWriter(new FileWriter(filePath,true));
  buff.write(measurementnumber+","+measurement.mytoString());
  buff.close();
}


/**
* Draws a time vs concentration plot using the file at filePath as input and returns it.
* @return GPlot of the data set.
*/
GPlot drawGraph(String filePath){
  Table table = loadTable(filePath,"header, csv");
  int nPoints = table.getRowCount();
  GPointsArray points = new GPointsArray(nPoints);
  float maxConcentration = 0;
  for(int i = 0; i < nPoints; i++){
    float tempConcentration = table.getRow(i).getFloat("Concentration");
    points.add(i*5,tempConcentration);
    if(maxConcentration < table.getRow(i).getFloat("Concentration")){
      maxConcentration = tempConcentration;
    } 
    
  }
  GPointsArray pointsDeviationPlus = new GPointsArray(nPoints);
  for(int i = 0; i < nPoints; i++){
    float tempConcentration = table.getRow(i).getFloat("Concentration");
    float tempDeviationPlus = table.getRow(i).getFloat("ConcentrationDeviation");
    pointsDeviationPlus.add(i*5,tempConcentration*tempConcentration*tempDeviationPlus);
  }
  
  GPointsArray pointsDeviationMinus = new GPointsArray(nPoints);
  for(int i = 0; i < nPoints; i++){
    float tempConcentration = table.getRow(i).getFloat("Concentration");
    float tempDeviationMinus = table.getRow(i).getFloat("ConcentrationDeviation");
    pointsDeviationMinus.add(i*5,tempConcentration*tempConcentration*tempDeviationMinus);
  }
  
  
  GPlot plot = new GPlot(this);
  plot.setBoxBgColor(color(0xff,0xff,0xff));
  plot.setDim(400,300);
  
  plot.setTitleText("Measured concentration over time");
  plot.getTitle().setFontColor(color(0x3c,0x7c,0xb9));
  plot.getTitle().setFontSize(18);
  plot.setBoxLineColor(255);
  plot.drawHorizontalLine((float) thresholdReaction,color(0x51,0xa7,0xf9),2);
  plot.getXAxis().setAxisLabelText("Time (min)");
  plot.getXAxis().setLineColor(color(0x3c,0x7c,0xb9));
  plot.getXAxis().setAllFontProperties("Helvetica",color(0x78,0x78,0x78),15);
  plot.getYAxis().setAxisLabelText("Concentration");
  plot.getYAxis().setAllFontProperties("Helvetica",color(0x78,0x78,0x78),15);
  plot.getYAxis().setLineColor(color(0x3c,0x7c,0xb9));
  plot.setXLim(0,table.getRowCount()*5+2);
  plot.setYLim(0,maxConcentration+0.01*maxConcentration);
  plot.setPoints(points);
  plot.setLineColor(color(0x51,0xa7,0xf9));
  plot.setPointColor(color(0x3c,0x7c,0xb9));
  return plot;
}