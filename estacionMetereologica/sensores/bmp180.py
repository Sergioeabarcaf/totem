import Adafruit_BMP.BMP085 as BMP085

def getPress():
    sensor = BMP085.BMP085()
    aux = sensor.read_pressure()
    return  {'presion': aux}
