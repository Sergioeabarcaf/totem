#!/usr/bin/python
# -*- coding: latin-1 -*-

# Programa de ejemplo de lectura de sensor barómetro

# Se prueba medir la presión atmosférica, la temperatura y la altitud, con el
# sensor barómetro BMP180.

# Para este ejemplo, el sensor BMP180 se conecta de la siguiente forma, según
# numeración BCM, según numeración BCM.
# BMP180 -> Raspberry Pi
# DA(SDA) -> SDA
# CL(SCL) -> SCL
# -(GND) -> GND
# +(VCC) -> 3,3V

# Fecha: Sábado, 13 de Mayo del 2017
# Autora: Helene Schmelzer Grez

#Modificado 14 de Junio del 2017
#Por: Francis Soto

# Bibliotecas incluidas
import Adafruit_BMP.BMP085 as BMP085
from time import sleep

while(True):
	sensor = BMP085.BMP085()

# Código Principal
	print ('Temperatura = {0:0.2f} *C' .format (sensor.read_temperature ()))
	print ('Presión = {0:0.2f} Pa' .format (sensor.read_pressure ()))
	print ('Altitud = {0:0.2f} m' .format (sensor.read_altitude ()))
	print ('Presión nivel del mar = {0:0.2f} Pa' .format (sensor.read_sealevel_pressure ()))
	print ('-------------------------------------')
	sleep(5)
# Resultados
# Temperatura = 19.40 *C
# Presión = 95664.00 Pa
# Altitud = 483.04 m
# Presión nivel del mar = 95662.00 Pa
