from flask import Flask
from flask_mqtt import Mqtt
app = Flask(__name__)

app.config['MQTT_BROKER_URL'] = '127.0.0.1'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
mqtt = Mqtt(app)

my_json = "{ 'connect_A' : '/dev/ttyUSB0', 'connect_B' : '/dev/ttyUSB1' }"

@app.route('/')
def index():
    return 'hello world'
    
@app.route('/api/v1.0/connect/', methods=['GET'])
def get_task():
    mqtt.publish('mytopic', my_json )
    return 'data was published'

if __name__ == '__main__':
    app.run(debug=True)