# import eventlet
# import json
from flask import Flask, render_template
from flask_mqtt import Mqtt
import time 
import pyrebase
# from flask_socketio import Socket
# from flask_bootstrap import Bootstrap

# eventlet.monkey_patch()

# For Firebase JS SDK v7.20.0 and later, measurementId is optional
firebaseConfig = {
  "apiKey": "AIzaSyBfoC8pByFL8ULmxInIoWHCcQTvfN75PNk",
  "authDomain": "minipro1-6178f.firebaseapp.com",
  "databaseURL": "https://minipro1-6178f-default-rtdb.firebaseio.com",
  "projectId": "minipro1-6178f",
  "storageBucket": "minipro1-6178f.appspot.com",
  "messagingSenderId": "35900511053",
  "appId": "1:35900511053:web:da3dccff2581e0a6c15d04",
  "measurementId": "G-ZHRL0HJWQF"
};
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

app = Flask(__name__)
# app.config['SECRET'] = 'my secret key'
# app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = 'mqtt.flespi.io'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = 'FlespiToken lCG8yJPUWRc9awe3M2AaTuKcqd5N4Nvgd1cByPklwkiuGmogcOgW6QWmURXOujSx'
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_REFRESH_TIME'] = 1.0
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False
app.config['MQTT_CLEAN_SESSION'] = True

# Parameters for SSL enabled
# app.config['MQTT_BROKER_PORT'] = 8883
# app.config['MQTT_TLS_ENABLED'] = True
# app.config['MQTT_TLS_INSECURE'] = True
# app.config['MQTT_TLS_CA_CERTS'] = 'ca.crt'

mqtt = Mqtt(app)
# socketio = SocketIO(app)
# bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


# @socketio.on('publish')
# def handle_publish(json_str):
#     data = json.loads(json_str)
#     mqtt.publish(data['topic'], data['message'])


# @socketio.on('subscribe')
# def handle_subscribe(json_str):
#     data = json.loads(json_str)
#     mqtt.subscribe(data['topic'])


# @socketio.on('unsubscribe_all')
# def handle_unsubscribe_all():
#     mqtt.unsubscribe_all()

@mqtt.on_connect()#
def handle_mqtt_connect(client,userdata,flags,rc):#
    print("MQTT broker connect")#
    mqtt.subscribe("minipro")#
    
@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print(data['topic'])    #
    print(data['payload']) #
    obj = data["payload"]
    t = obj.split()
    
   
    
    db.child("temp").update({"obj0":t[0]})
    x0 = t[0]
    db.child("humidity").update({"obj1":t[1]})
    x1 = t[1]
    db.child("rain").update({"obj2":t[2]})
    x2 = t[2]
    # socketio.emit('mqtt_message', data=data)

# @mqtt.on_log()
# def handle_logging(client, userdata, level, buf):
#     print(level, buf)


# if __name__ == '__main__':
#     # important: Do not use reloader because this will create two Flask instances.
#     # Flask-MQTT only supports running with one instance
#     socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=False)