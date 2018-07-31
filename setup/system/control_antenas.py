#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

GPIO.output(17, not GPIO.input(17))

sys.exit()

