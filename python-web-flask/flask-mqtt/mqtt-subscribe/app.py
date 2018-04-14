from flask import Flask
from flask_mqtt import Mqtt
import json
app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = '127.0.0.1'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_REFRESH_TIME'] = 3.0  # refresh time in seconds
mqtt = Mqtt(app)

@app.route('/')
def index():
    return 'hello world'

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('mytopic')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    # topic=message.topic
    payload= message.payload.decode()
    p = json.loads(payload)
    print("-------msg-------")
    print('name  :', p['name'])
    print('email :', p['email'])

if __name__ == '__main__':
    app.run(debug=True)