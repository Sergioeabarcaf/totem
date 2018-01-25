import os
import time
import sys

#time.sleep(80)
date = open("/home/pi/totem/nodejs/time/h.txt")
line = date.readline()
date.close()
os.system("sudo date +%H -s "+line)
date = open("/home/pi/totem/nodejs/time/dmy.txt")
line = date.readline()
date.close()
os.system("sudo date +%Y%m%d -s "+line)
sys.exit()
