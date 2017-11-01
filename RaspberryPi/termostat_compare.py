
import RPi.GPIO as GPIO
import smbus
import time
import subprocess
from TMP006 import TMP006

'''
Script for running the Thermocycling device at a certain temperature as decleared below
'''
desired_temperature=85


# Get I2C bus
bus = smbus.SMBus(1)



GPIO.setmode(GPIO.BOARD)

ControlPin = [35]

for pin in ControlPin:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,0)

a=TMP006()
a.begin()

number_of_seconds=1000
temp_target=desired_temperature
##### THERMO STAT #### 
for i in range(0,number_of_seconds):
	time.sleep(0.3)
	a=TMP006()
	cTemp=a.readObjTempC()
	print "Temperature in Celsius is : %.2f C" %cTemp
	if cTemp > temp_target:
		GPIO.output(ControlPin[0],1)
	else:
		GPIO.output(ControlPin[0],0)
	time.sleep(0.7)

GPIO.cleanup()
