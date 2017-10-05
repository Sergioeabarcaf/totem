#!/usr/bin/env python

import sys
import Adafruit_DHT as sensor

humedad, temperatura = sensor.read_retry(sensor.AM2302, 24)

print humedad
print temperatura

sys.exit()
