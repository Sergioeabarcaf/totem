import time
import sys

f=open('datalog.txt','a')
f.write(time.strftime("%c") + "\n")
f.close()
sys.exit()
