import os
import time
import sys

os.system(ssh turismo@192.168.252.250 'date "+%Y%m%d %T"'`")

"ssh turismo@192.168.252.250 'date "+%Y%m%d %T"'"

date = open("time.txt")
line = date.readline()
print(line)
date.close()

time.sleep(3)
os.system("sudo date +%Y%m%d%T -s '"+line+"'")
sys.exit()
