import serial
import time

def getArduino():
    datos = {
        'lummens' : 0,
        'uv': 0,
        'viend_ins_grado': 0,
        'viend_chr': 0,
        'viend_2m_grados': 0,
        'vel_2m':0,
        'raf_ins':0,
        'raf_10m':0,
        'raf_ins_grados':0,
        'raf_10m_grados':0,
        'lluvia_1h':0,
        'lluvia_24h':0
        }

    #Configuracion del puerto donde se encuentra conectado el arduino.
    arduino_txrx = serial.Serial('/dev/ttyACM0', 115200)

    for i in range(0,2):
        print i
        #Se agrega una pausa de 2s a la espera del fin de la comunicacion entre dispositivos.
        time.sleep(2)

        #Se indica al arduino el inicio de la transmision de datos.
        arduino_txrx.write('t')

        #se espera al inicio de la transmision.
        while arduino_txrx.inWaiting()==0:
            pass

        info = arduino_txrx.readline()
        try:
            info = float(info)
        except ValueError:
            info = info.strip(' \t\r\n')
        datos['lummens'] = info

        #A continuacion el indice UV:
        info = arduino_txrx.readline()
        try:
            info = float(info)
        except ValueError:
            info = info.strip(' \t\r\n')
        datos['uv'] = info
        #A continuacion direccion del viento instantanea:
        info = arduino_txrx.readline()
        try:
            info = float(info)
        except ValueError:
            info = info.strip(' \t\r\n')
        datos['viend_ins_grado'] = info
        #A continuacion la direccion del viento direccion cardinal:
        info = arduino_txrx.readline()
        try:
            info = float(info)
        except ValueError:
            info = info.strip(' \t\r\n')
        datos['viend_chr'] = info
        #A continuacion la direccion del viento promedio de los 2 ultimos minutos:
        info = arduino_txrx.readline()
        try:
            info = float(info)
        except ValueError:
            info = info.strip(' \t\r\n')
        datos['viend_2m_grados'] = info
        #A continuacion la velocidad del viento promedio de los 2 ultimos minutos:
        info = arduino_txrx.readline()
        try:
            info = float(info)
        except ValueError:
            info = info.strip(' \t\r\n')
        datos['vel_2m'] = info
        #A continuacion la velocidad del viento instantanea:
        info = arduino_txrx.readline()
        try:
            info = float(info)
        except ValueError:
            info = info.strip(' \t\r\n')
        datos['raf_ins'] = info
        #A continuacion la velocidad del viento promedio de los 10 ultimos minutos:
        info = arduino_txrx.readline()
        try:
            info = float(info)
        except ValueError:
            info = info.strip(' \t\r\n')
        datos['raf_10m'] = info
        #A continuacion la direccion de la rafaga de viento instantanea:
        info = arduino_txrx.readline()
        try:
            info = float(info)
        except ValueError:
            info = info.strip(' \t\r\n')
        datos['raf_ins_grados'] = info
        #A continuacion la direccion de la rafaga de viento promedio de los ultimos 10 minutos:
        info = arduino_txrx.readline()
        try:
            info = float(info)
        except ValueError:
            info = info.strip(' \t\r\n')
        datos['raf_10m_grados'] = info
        #A continuacion la cantidad de lluvia caida en la ultima hora:
        info = arduino_txrx.readline()
        try:
            info = float(info)
        except ValueError:
            info = info.strip(' \t\r\n')
        datos['lluvia_1h'] = info
        #Finalmente la cantidad de lluvia caida en las ultimas 24 horas:
        info = arduino_txrx.readline()
        try:
            info = float(info)
        except ValueError:
            info = info.strip(' \t\r\n')
        datos['lluvia_24h'] = info

    arduino_txrx.close()
    return datos
