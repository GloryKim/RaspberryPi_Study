# -*- coding: utf-8 -*-
#!/usr/local/bin/python

import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM)

print "Set up Motor pins as output"

GPIO.setup(23, GPIO.OUT)

try:
    while True:
        GPIO.output(23, False)
        time.sleep(2)
        GPIO.output(23,True)
        time.sleep(2)
        
except KeyboardInterrupt:
    GPIO.cleanup()