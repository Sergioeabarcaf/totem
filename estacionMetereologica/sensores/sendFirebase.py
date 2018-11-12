import am2302
import bmp180
import comunicacion_ok
import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def send(data):
    ref = db.reference('data')
    ref.push(data)

data = {}
data.update(bmp180.getPress(),)
data.update(am2302.getTemHum())
data.update(comunicacion_ok.getArduino())
data.update({'timestamp': str(datetime.datetime.utcnow())})

cred = credentials.Certificate('keyTurismo.json')
default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://turismo-5351f.firebaseio.com/'
})

send(data)
