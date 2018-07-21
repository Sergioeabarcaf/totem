#!/usr/bin/env python

import sys
import Adafruit_DHT as sensor
import math

humedad, temperatura = sensor.read_retry(sensor.AM2302, 24)
#pt_rocio= temperatura + 35*math.log10(humedad/100)
#alt_nube=122*(temperatura - pt_rocio)
print "humedad: " + str(humedad)+"%"
print "temperatura: "+ str(temperatura)+"*C"
#print "Punto de Rocio: " + str(pt_rocio)+"*C"
#print "Altura de Nubes: " + str(alt_nube)+"mts"
sys.exit()
