import RPi.GPIO as GPIO
import time

'''

Script for running our peristaltic pump for a certain amount of turns
a turn is equivalent to 15-30 µl
'''

number_of_turns=600


GPIO.setmode(GPIO.BOARD)

ControlPin = [11,13,15,16]

ControlPin2 = [32,29,31,33]


for pin in ControlPin:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,0)

for pin in ControlPin2:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,0)








x=512*number_of_turns

seq = [
	[1,0,0,0],
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,1],
	[0,0,0,1],
	[1,0,0,1] ]

for i in range(x):
	for halfstep in range(8):
		for pin in range(4):
			GPIO.output(ControlPin[pin], seq[halfstep][pin])
			GPIO.output(ControlPin2[pin], seq[6-halfstep][pin])
		time.sleep(0.0010)	




GPIO.cleanup()

	
