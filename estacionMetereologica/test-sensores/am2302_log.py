#!/usr/bin/python
# exterior

import sys
import Adafruit_DHT as sensor
from datetime import datetime

humedad, temperatura = sensor.read_retry(sensor.AM2302, 24)
strHum = "humedad: "+str(humedad)
strTem = "temperatura: "+str(temperatura)
strLog = "\n"+str(datetime.now())+" "+ strHum + strTem

log=open("log/am2302.log","ab")
log.write(strLog)
log.close()

print strLog

sys.exit()
