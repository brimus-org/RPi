#!/usr/bin/python
import RPi.GPIO as GPIO

pin_list = [40]

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(pin_list, GPIO.OUT)

GPIO.setup(pin_list, GPIO.HIGH)
