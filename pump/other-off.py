#!/usr/bin/python
import RPi.GPIO as GPIO

pin = 35

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(pin, GPIO.OUT)

GPIO.setup(pin, GPIO.HIGH)
