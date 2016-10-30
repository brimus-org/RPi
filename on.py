#!/usr/bin/python
import RPi.GPIO as GPIO

relay_pins = {'one':18, 'two':16}

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

for relay_pin, board_pin in relay_pins.iteritems():
	GPIO.setup(board_pin, GPIO.OUT)
	GPIO.output(board_pin, GPIO.LOW) 
