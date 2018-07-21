#!/usr/bin/python

import sys
import Adafruit_DHT as sensor
from datetime import datetime

humedad, temperatura = sensor.read_retry(sensor.AM2302, 24)

log=open("temp.log","ab")
log.write("\n"+str(datetime.now())+" "+"temperatura: "+str(temperatura))
log.close()

sys.exit()

