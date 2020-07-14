import paho.mqtt.client as mqtt
import sys
import uuid

broker = '78rjuux.mqtt.iot.bj.baidubce.com'
port = 1883
username = '78rjuux/mylight'
password = 'RJw9eByMUVnfDCwY'
clientid = 'test_mqtt_python_' + str(uuid.uuid4())
topic = '$baidu/iot/shadow/mylight/update'


def on_connect(client, userdata, rc):
    print("Connection returned " + str(rc))
def on_message(client, userdata, msg):
    msg = str(msg.payload).encode('utf-8')
    print('MQTT message received: ' + msg)
    if msg == 'exit':
        sys.exit()


client = mqtt.Client(clientid)
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username, password)

print('Connecting to broker: ' + broker)
client.connect(broker, port)
on_connect()
client.loop_forever()

