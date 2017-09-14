import os
import time

"""
while(True):
    os.system("sudo python /home/pi/totem/Est_Met/sensores/altura.py")
    os.system("sudo python3 /home/pi/totem/Est_Met/sensores/humedad.py")
    os.system("sudo python /home/pi/totem/Est_Met/sensores/nivel_mar.py")
    os.system("sudo python /home/pi/totem/Est_Met/sensores/presion.py")
    os.system("sudo python3 /home/pi/totem/Est_Met/sensores/pun_rocio.py")
    os.system("sudo python /home/pi/totem/Est_Met/sensores/temperatura_BMP085.py")
    os.system("sudo python3 /home/pi/totem/Est_Met/sensores/temperatura.py")
    os.system("sudo python /home/pi/totem/Est_Met/sensores/comunicacion_ok.py")
    time.sleep(30)
"""

os.system("sudo python3 /home/pi/totem/Est_Met/sensores/altura.py")
os.system("python3 /home/pi/totem/Est_Met/sensores/humedad.py")
os.system("sudo python3 /home/pi/totem/Est_Met/sensores/nivel_mar.py")
os.system("sudo python3 /home/pi/totem/Est_Met/sensores/presion.py")
os.system("python3 /home/pi/totem/Est_Met/sensores/pun_rocio.py")
os.system("sudo python3 /home/pi/totem/Est_Met/sensores/temperatura_BMP085.py")
os.system("python3 /home/pi/totem/Est_Met/sensores/temperatura.py")
os.system("sudo python3 /home/pi/totem/Est_Met/sensores/comunicacion_ok.py")
