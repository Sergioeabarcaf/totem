import os
import time
import sys

f=open('timelog.txt','a')
f.write(time.strftime("%c") + "\n")
f.close()
time.sleep(10)
os.system('sudo node /home/pi/totem/nodejs/app.js &')
sys.exit()
