import am2302
import bmp180
import comunicacion_ok
import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def send(data,date):
    dateAux = date.split(" ")
    date = dateAux[0].split("-")
    dir = str("data/A" + date[0] + "/M" + date[1] + "/D" + date[2])
    ref = db.reference(dir)
    ref.push(data)

date = str(datetime.datetime.utcnow())

data = {}
data.update(bmp180.getPress())
data.update(am2302.getTemHum())
data.update(comunicacion_ok.getArduino())
data.update({'timestamp': str(datetime.datetime.utcnow())})

cred = credentials.Certificate('/home/pi/totem/estacionMetereologica/sensores/keyTurismo.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://turismo-5351f.firebaseio.com/'
})

send(data, date)
