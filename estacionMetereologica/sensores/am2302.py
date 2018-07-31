#!/usr/bin/env python

import os
import sys
import Adafruit_DHT as sensor
host = "192.168.150.2" #Direccion IP de donde esta alojado el servidor MQTT
port = "1883" #Puerto por defecto del servidor MQTT
humedad, temperatura = sensor.read_retry(sensor.AM2302, 24)

humedad = round(float(humedad),2)
temperatura = round(float(temperatura),2)

menHum = "totem1/" + str(humedad)
menTem = "totem1/" + str(temperatura)

os.system("mosquitto_pub -t temperatura -m " + menTem + " -h " + host + " -p " + port)
os.system("mosquitto_pub -t humedad -m " + menHum + " -h " + host + " -p " + port)

sys.exit()
