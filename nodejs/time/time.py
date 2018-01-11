import os
import time
import sys

#time.sleep(80)
date = open("/home/pi/totem/nodejs/time/time.txt")
line = date.readline()
date.close()
os.system("sudo date +%Y%m%d%T -s '"+line+"'")
sys.exit()
