# Programacion para la obtencion de informacion desde una tarjeta de desarrollo Arduino Uno desde
# una Raspberry Pi 3 modelo B.

import os
import serial
import time
import sys
import json

host = "192.168.150.2" #Direccion IP de donde esta alojado el servidor MQTT
hostNC = "192.168.252.250" #Direccion IP de donde esta alojado el servidor MQTT nodo central
port = "1883" #Puerto por defecto del servidor MQTT


#diccionario donde se acumularan los valores de las variables medidas por un Arduino.
datos = {
    'lumens' : 0,
    'uv': 0,
    'viend_ins_grado': 0,
    'viend_chr': 0,
    'viend_2m_grados': 0,
    'vel_2m':0,
    'raf_ins':0,
    'raf_10m':0,
    'raf_ins_grados':0,
    'raf_10m_grados':0,
    'lluvia_1h':0,
    'lluvia_24h':0}

#Configuracion del puerto donde se encuentra conectado el arduino.
arduino_txrx = serial.Serial('/dev/ttyACM0', 115200)
#Se agrega una pausa de 2s a la espera del fin de la comunicacion entre dispositivos.
time.sleep(2)

#Se indica al arduino el inicio de la transmision de datos.
arduino_txrx.write('t')

#se espera al inicio de la transmision.
while arduino_txrx.inWaiting()==0:
    pass

#comienza la transmision en roden, de modo de guardar cada dato en la ubicacion que le corresponda en el diccionario
#Se inicia con la intensidad luminica:
info = arduino_txrx.readline()
try:
    info = float(info)
except ValueError:
    info = info.strip(' \t\r\n')
datos['lumens'] = info
#A continuacion el indice UV:
info = arduino_txrx.readline()
try:
    info = float(info)
except ValueError:
    info = info.strip(' \t\r\n')
datos['uv'] = info
#A continuacion direccion del viento instantanea:
info = arduino_txrx.readline()
try:
    info = float(info)
except ValueError:
    info = info.strip(' \t\r\n')
datos['viend_ins_grado'] = info
#A continuacion la direccion del viento direccion cardinal:
info = arduino_txrx.readline()
try:
    info = float(info)
except ValueError:
    info = info.strip(' \t\r\n')
datos['viend_chr'] = info
#A continuacion la direccion del viento promedio de los 2 ultimos minutos:
info = arduino_txrx.readline()
try:
    info = float(info)
except ValueError:
    info = info.strip(' \t\r\n')
datos['viend_2m_grados'] = info
#A continuacion la velocidad del viento promedio de los 2 ultimos minutos:
info = arduino_txrx.readline()
try:
    info = float(info)
except ValueError:
    info = info.strip(' \t\r\n')
datos['vel_2m'] = info
#A continuacion la velocidad del viento instantanea:
info = arduino_txrx.readline()
try:
    info = float(info)
except ValueError:
    info = info.strip(' \t\r\n')
datos['raf_ins'] = info
#A continuacion la velocidad del viento promedio de los 10 ultimos minutos:
info = arduino_txrx.readline()
try:
    info = float(info)
except ValueError:
    info = info.strip(' \t\r\n')
datos['raf_10m'] = info
#A continuacion la direccion de la rafaga de viento instantanea:
info = arduino_txrx.readline()
try:
    info = float(info)
except ValueError:
    info = info.strip(' \t\r\n')os.system("mosquitto_pub -t "+ t0 + " -m " + v0 + " -h " + host + " -p " + port)
datos['raf_ins_grados'] = info
#A continuacion la direccion de la rafaga de viento promedio de los ultimos 10 minutos:
info = arduino_txrx.readline()
try:
    info = float(info)
except ValueError:
    info = info.strip(' \t\r\n')
datos['raf_10m_grados'] = info
#A continuacion la cantidad de lluvia caida en la ultima hora:
info = arduino_txrx.readline()
try:
    info = float(info)
except ValueError:
    info = info.strip(' \t\r\n')
datos['lluvia_1h'] = info
#Finalmente la cantidad de lluvia caida en las ultimas 24 horas:
info = arduino_txrx.readline()
try:
    info = float(info)
except ValueError:
    info = info.strip(' \t\r\n')
datos['lluvia_24h'] = info

os.system("mosquitto_pub -t lumens" + " -m totem1/" + str(datos['lumens']) + " -h " + host + " -p " + port)
os.system("mosquitto_pub -t uv" + " -m totem1/" + str(datos['uv']) + " -h " + host + " -p " + port)
os.system("mosquitto_pub -t viend_ins_grado" + " -m totem1/" + str(datos['viend_ins_grado']) + " -h " + host + " -p " + port)
os.system("mosquitto_pub -t viend_chr" + " -m totem1/" + str(datos['viend_chr']) + " -h " + host + " -p " + port)
os.system("mosquitto_pub -t viend_2m_grados" + " -m totem1/" + str(datos['viend_2m_grados']) + " -h " + host + " -p " + port)
os.system("mosquitto_pub -t vel_2m" + " -m totem1/" + str(datos['vel_2m']) + " -h " + host + " -p " + port)
os.system("mosquitto_pub -t raf_ins" + " -m totem1/" + str(datos['raf_ins']) + " -h " + host + " -p " + port)
os.system("mosquitto_pub -t raf_10m" + " -m totem1/" + str(datos['raf_10m']) + " -h " + host + " -p " + port)
os.system("mosquitto_pub -t raf_ins_grados" + " -m totem1/" + str(datos['raf_ins_grados']) + " -h " + host + " -p " + port)
os.system("mosquitto_pub -t raf_10m_grados" + " -m totem1/" + str(datos['raf_10m_grados']) + " -h " + host + " -p " + port)
os.system("mosquitto_pub -t lluvia_1h" + " -m totem1/" + str(datos['lluvia_1h']) + " -h " + host + " -p " + port)
os.system("mosquitto_pub -t lluvia_24h" + " -m totem1/" + str(datos['lluvia_24h']) + " -h " + host + " -p " + port)

os.system("mosquitto_pub -t lumens" + " -m totem1/" + str(datos['lumens']) + " -h " + hostNC + " -p " + port)
os.system("mosquitto_pub -t uv" + " -m totem1/" + str(datos['uv']) + " -h " + hostNC + " -p " + port)
os.system("mosquitto_pub -t viend_ins_grado" + " -m totem1/" + str(datos['viend_ins_grado']) + " -h " + hostNC + " -p " + port)
os.system("mosquitto_pub -t viend_chr" + " -m totem1/" + str(datos['viend_chr']) + " -h " + hostNC + " -p " + port)
os.system("mosquitto_pub -t viend_2m_grados" + " -m totem1/" + str(datos['viend_2m_grados']) + " -h " + hostNC + " -p " + port)
os.system("mosquitto_pub -t vel_2m" + " -m totem1/" + str(datos['vel_2m']) + " -h " + hostNC + " -p " + port)
os.system("mosquitto_pub -t raf_ins" + " -m totem1/" + str(datos['raf_ins']) + " -h " + hostNC + " -p " + port)
os.system("mosquitto_pub -t raf_10m" + " -m totem1/" + str(datos['raf_10m']) + " -h " + hostNC + " -p " + port)
os.system("mosquitto_pub -t raf_ins_grados" + " -m totem1/" + str(datos['raf_ins_grados']) + " -h " + hostNC + " -p " + port)
os.system("mosquitto_pub -t raf_10m_grados" + " -m totem1/" + str(datos['raf_10m_grados']) + " -h " + hostNC + " -p " + port)
os.system("mosquitto_pub -t lluvia_1h" + " -m totem1/" + str(datos['lluvia_1h']) + " -h " + hostNC + " -p " + port)
os.system("mosquitto_pub -t lluvia_24h" + " -m totem1/" + str(datos['lluvia_24h']) + " -h " + hostNC + " -p " + port)
#creamos un archivo en formato json donde se agregan la informacion acumulada en el diccionario "datos" para el envio de la informacion a una base de datos:
with open('datos_arduino.jason','w') as archivo:
        json.dump(datos,archivo)

#Finalmente se cierra la comunicacion serie del puerto USB y se finaliza la ejecucion del script python:
arduino_txrx.close()
sys.exit()
