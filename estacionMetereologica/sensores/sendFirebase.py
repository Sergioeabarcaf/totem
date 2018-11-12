import am2302
import bmp180
import comunicacion_ok

data = {}

data.update(bmp180.getPress())
data.update(am2302.getTemHum())
data.update(comunicacion_ok.getArduino())


print data
