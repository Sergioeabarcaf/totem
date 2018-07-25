import os
import time
import sys

host = "192.168.150.2"
port = "1883"

os.system("sudo python /home/pi/totem/estacionMetereologica/sensores/am2302_temp.py")
os.system("sudo python /home/pi/totem/estacionMetereologica/sensores/presion.py")
os.system("sudo python /home/pi/totem/estacionMetereologica/sensores/comunicacion_ok.py")

