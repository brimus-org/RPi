#!/usr/bin/python
import RPi.GPIO as GPIO

pin_list = [13,15]

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(pin_list, GPIO.IN)
#GPIO.setup(pin_list, GPIO.OUT)

#for pin in pin_list:
print 'PIN = 13'
print GPIO.input(13)
print 'PIN = 15'
print GPIO.input(15)
	

