import os
import time

while(True):
    #horactual = time.time()
    os.system("sudo python /home/pi/totem/Est_Met/sensores/am2302_temp.py")
    #os.system("sudo python /home/pi/totem/Est_Met/sensores/altura.py")
    #os.system("sudo python3 /home/pi/totem/Est_Met/sensores/humedad.py")
    #os.system("sudo python /home/pi/totem/Est_Met/sensores/nivel_mar.py")
    os.system("sudo python /home/pi/totem/Est_Met/sensores/presion.py")
    #os.system("sudo python3 /home/pi/totem/Est_Met/sensores/pun_rocio.py")
    #os.system("sudo python /home/pi/totem/Est_Met/sensores/temperatura_BMP085.py")
    #os.system("sudo python3 /home/pi/totem/Est_Met/sensores/temperatura.py")
    os.system("sudo python /home/pi/totem/Est_Met/sensores/comunicacion_ok.py")
    #print(time.time() - horactual)
    time.sleep(60)


