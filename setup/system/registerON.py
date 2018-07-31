import os
import time
import sys

# time.sleep(60)
f=open('log/dateON.log','a')
f.write(time.strftime("%c") + "\n")
f.close()
sys.exit()
