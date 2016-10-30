#!/usr/bin/python

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
timeout = 0.020

while 1:
        GPIO.setup(13, GPIO.OUT)
        #cleanup output
        GPIO.output(13, 0)

        time.sleep(0.000002)

        #send signal
        GPIO.output(13, 1)

        time.sleep(0.000005)

        GPIO.output(13, 0)

        GPIO.setup(13, GPIO.IN)
        
        goodread=True
        watchtime=time.time()
        while GPIO.input(13)==0 and goodread:
                starttime=time.time()
                if (starttime-watchtime > timeout):
                        goodread=False

        if goodread:
                watchtime=time.time()
                while GPIO.input(13)==1 and goodread:
                        endtime=time.time()
                        if (endtime-watchtime > timeout):
                                goodread=False
        
        if goodread:
                duration=endtime-starttime
                distance=duration*34000/2
                print distance
