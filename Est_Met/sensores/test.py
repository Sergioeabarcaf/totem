import os
import time

time.sleep(30)
os.system("sudo python /home/pi/totem/Est_Met/sensores/am2302_temp.py")
os.system("sudo python /home/pi/totem/Est_Met/sensores/presion.py")
os.system("sudo python /home/pi/totem/Est_Met/sensores/comunicacion_ok.py")
