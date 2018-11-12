import am2302
import bmp180
import comunicacion_ok

data = {}

data.append(bmp180.getPress())
data.append(am2302.getTemHum())
data.append(comunicacion_ok.getArduino())


print data
