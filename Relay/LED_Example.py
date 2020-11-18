# -*- coding: utf-8 -*-
#!/usr/local/bin/python

import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM)

print "Set up Motor pins as output"

GPIO.setup(14, GPIO.OUT)

try:
    while True:
        GPIO.output(14, False)
        time.sleep(1)
        GPIO.output(14,True)
        print("Start")
        time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup()