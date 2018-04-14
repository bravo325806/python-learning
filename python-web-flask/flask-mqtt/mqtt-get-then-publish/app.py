from flask import Flask
from flask_mqtt import Mqtt
from flask import render_template
app = Flask(__name__)

app.config['MQTT_BROKER_URL'] = '127.0.0.1'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
mqtt = Mqtt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v1.0/tasks/<want_to_pub>', methods=['GET'])
def get_task(want_to_pub):
    if len(want_to_pub) == 0:
        abort(404)
    mqtt.publish('mytopic',want_to_pub )
    return want_to_pub

if __name__ == '__main__':
    app.run(debug=True)