import os
import time

while(True):
    os.system("sudo python /home/pi/totem/Est_Met/sensores/am2302_temp.py")
    os.system("sudo python /home/pi/totem/Est_Met/sensores/presion.py")
    os.system("sudo python /home/pi/totem/Est_Met/sensores/comunicacion_ok.py")
    time.sleep(5)
