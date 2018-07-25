#!/usr/bin/python
# interior

import sys
import Adafruit_DHT as sensor
from datetime import datetime

humedad, temperatura = sensor.read_retry(sensor.DHT11, 21)

log=open("temp.log","ab")
log.write("\n"+str(datetime.now())+" "+"temperatura: "+str(temperatura)+" "+"humedad: "+str(humedad))
log.close()

sys.exit()
