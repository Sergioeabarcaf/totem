import Adafruit_DHT as sensor

def getTemHum():
    humedad, temperatura = sensor.read_retry(sensor.AM2302, 24)
    humedad = round(float(humedad),2)
    temperatura = round(float(temperatura),2)
    return {"temperatura":temperatura, "humedad":humedad}
