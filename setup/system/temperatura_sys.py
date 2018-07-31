#!/usr/bin/python

import sys
import Adafruit_DHT as sensor
from datetime import datetime
import commands

tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
temp_pi_cpu = tempFile.read()
tempFile.close()
temp_pi_cpu=float(temp_pi_cpu)/1000

temp_pi_gpu=commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp').replace('temp=',' ')

log=open("/home/pi/totem/log/tempSystem.log","ab")
log.write("\n"+str(datetime.now())+" "+"temperatura CPU: "+str(temp_pi_cpu)+" "+"temperatura GPU: "+str(temp_pi_gpu))
log.close()

sys.exit()
