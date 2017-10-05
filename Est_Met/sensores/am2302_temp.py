#!/usr/bin/env python

import os
import sys
import Adafruit_DHT as sensor
host = "192.168.251.20" #Direccion IP de donde esta alojado el servidor MQTT
port = "1883" #Puerto por defecto del servidor MQTT
humedad, temperatura = sensor.read_retry(sensor.AM2302, 24)

menHum = "totem1/" + str(round(humedad,2))
menTem = "totem1/" + str(round(temperatura,2))

os.system("mosquitto_pub -t temperatura -m " + menTem + " -h " + host + " -p " + port)
os.system("mosquitto_pub -t humedad -m " + menHum + " -h " + host + " -p " + port)

sys.exit()
