import RPi.GPIO as GPIO
import smbus
import time
import subprocess

'''
Script for running the second thermoelement at a certain temperature target
'''
desired_temperature=37

# Get I2C bus
bus = smbus.SMBus(1)

bus.write_byte(0x40, 0xF3)
time.sleep(0.3)

# SI7021 address, 0x40(64)
# Read data back, 2 bytes, Temperature MSB first
data0 = bus.read_byte(0x40)
data1 = bus.read_byte(0x40)

# Convert the data
cTemp = ((data0 * 256 + data1) * 175.72 / 65536.0) - 46.85
fTemp = cTemp * 1.8 + 32

# Output data to screen
print "Temperature in Celsius is : %.2f C" %cTemp



GPIO.setmode(GPIO.BOARD)

ControlPin = [37]

for pin in ControlPin:
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,0)
	



number_of_seconds=1000
temp_target=desired_temperature
##### THERMO STAT #### 
for i in range(0,number_of_seconds):
	bus.write_byte(0x40, 0xF3)
	time.sleep(0.3)
	data0 = bus.read_byte(0x40)
	data1 = bus.read_byte(0x40)
	cTemp = ((data0 * 256 + data1) * 175.72 / 65536.0) - 46.85
	print "Temperature in Celsius is : %.2f C" %cTemp
	if cTemp > temp_target:
		GPIO.output(ControlPin[0],1)
	else:
		GPIO.output(ControlPin[0],0)
	time.sleep(0.7)


GPIO.cleanup()
