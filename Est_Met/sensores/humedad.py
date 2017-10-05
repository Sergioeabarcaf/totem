#importar la libreria necesaria para el sensor
import os
from pi_sht1x import SHT1x
import RPi.GPIO as GPIO

host = "192.168.150.2" #Direccion IP de donde esta alojado el servidor MQTT
# hostNC = "192.168.252.250" #Direccion IP de donde esta alojado el servidor MQTT nodo central
port = "1883" #Puerto por defecto del servidor MQTT
t0 = 'humedad' #Direccion donde se envian los datos del sensor

#Lectura de datos entregadas por sensor
sensor=SHT1x(38, 40, gpio_mode=GPIO.BOARD)
fun_temp=sensor.read_temperature()
sensor.read_humidity(fun_temp)
aux = sensor.humidity
men = "totem1/" + str(aux)
#Publicacion de los datos del sensor al servidor MQTT
os.system("mosquitto_pub -t "+ t0 + " -m " + men + " -h " + host + " -p " + port)
# os.system("mosquitto_pub -t "+ t0 + " -m " + men + " -h " + hostNC + " -p " + port)
