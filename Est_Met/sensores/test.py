import os
import time
import sys

host = "192.168.150.2"
port = "1883"
uv = 2
men = "totem1/" + str(uv)

os.system("mosquitto_pub -t uv -m " + men + " -h " + host + " -p " + port)
#time.sleep(60)
os.system("sudo python /home/pi/totem/Est_Met/sensores/am2302_temp.py")
os.system("sudo python /home/pi/totem/Est_Met/sensores/presion.py")
os.system("sudo python /home/pi/totem/Est_Met/sensores/comunicacion_ok.py")

