import os
import time
import sys

time.sleep(60)
f=open('/home/pi/totem/log/dateON.log','a')
f.write(time.strftime("%c") + "\n")
f.close()
sys.exit()
