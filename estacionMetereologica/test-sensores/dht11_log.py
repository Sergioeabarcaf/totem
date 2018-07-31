#!/usr/bin/python
# interior

import sys
import Adafruit_DHT as sensor
from datetime import datetime

humedad, temperatura = sensor.read_retry(sensor.DHT11, 21)
strPrint = "\n"+str(datetime.now())+" "+"temperatura: "+str(temperatura)+" "+"humedad: "+str(humedad)

log=open("../../log/tempDHT11.log","ab")
log.write(strPrint)
log.close()

print strPrint

sys.exit()
