#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)

GPIO.output(4, not GPIO.input(4))

sys.exit()
