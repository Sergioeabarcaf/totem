# Programacion para la obtencion de informacion desde una tarjeta de desarrollo Arduino Uno desde
# una Raspberry Pi 3 modelo B.

import serial
import time
import sys

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

print "primera lectura"
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
print datos['viend_chr']
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
    info = info.strip(' \t\r\n')
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

time.sleep(2)

print "segunda lectura"
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
print datos['viend_chr']
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
    info = info.strip(' \t\r\n')
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



print (datos)

#Finalmente se cierra la comunicacion serie del puerto USB y se finaliza la ejecucion del script python:
arduino_txrx.close()
sys.exit()
