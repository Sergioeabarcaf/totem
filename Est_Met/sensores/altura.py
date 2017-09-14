#importar la libreria necesaria para el sensor
import os
import Adafruit_BMP.BMP085 as BMP085

host = "192.168.150.2" #Direccion IP de donde esta alojado el servidor MQTT
#hostNC = "192.168.252.250" #Direccion IP de donde esta alojado el servidor MQTT nodo central
port = "1883" #Puerto por defecto del servidor MQTT
t0 = 'altitud' #Direccion donde se envian los datos del sensor

#Lectura de datos entregadas por sensor
sensor = BMP085.BMP085()
aux = sensor.read_altitude()
men = "totem1/" + str(aux)
#Publicacion de los datos del sensor al servidor MQTT
os.system("mosquitto_pub -t "+ t0 + " -m " + men + " -h " + host + " -p " + port)
#os.system("mosquitto_pub -t "+ t0 + " -m " + men + " -h " + hostNC + " -p " + port)
