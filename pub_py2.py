import paho.mqtt.client as mqtt
import time
import json

a=1
str1=""
def on_publish(msg, rc):
    if rc == 0:
        print("publish success, msg = " + msg)

def on_connect(client, userdata, flags, rc):
    print("Connection returned " + str(rc))
    global a
    a=rc
    str1 = str(rc)
    print(str1)
def on_disconnect(client, userdata, rc):
    print("disconnect:rc="+str(rc))

def on_message(client, userdata, msg):
    #print(msg.topic+str(msg.payload.decode('utf-8')))
    #print(msg.topic + " " + ":" + str(msg.payload))
    print(str(msg.payload))
    global str1
    str1=str(msg.payload)
def on_subscribe(client, userdata, mid, granted_qos):
    print("On Subscribed: qos = %d" % granted_qos)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection %s" % rc)
client = mqtt.Client(client_id="test_mqtt_sender_1")


user = "78rjuux/mylight"
pwd = "wbcahpr13s2f3pwj"
endpoint = "78rjuux.mqtt.iot.bj.baidubce.com"
port = 1883
topic = "$baidu/iot/shadow/mylight/update"
topic1 = "$baidu/iot/shadow/mylight/update/accepted"
topic2 = "$baidu/iot/shadow/mylight/update/rejected"
def connect():
    client.username_pw_set(user, pwd)
    client.connect(endpoint, port, 60)
    client.on_connect = on_connect


    print('Connecting to broker: ' + endpoint)

    client.loop_start()
    time.sleep(2)

def pri():
    global a
    print("rc="+str(a))
    return  a

def pri1():
    global str1
    return str1
def disconnect():
    client.disconnect()
    client.on_disconnect=on_disconnect

def publish(strr):

    data = {"reported": {"light": strr}}
    msg = json.dumps(data)
    rc, mid = client.publish(topic, payload=str(msg), qos=0)  # qos
    on_publish(msg, rc)
    print(rc)
    time.sleep(2)

def subscribe():
    client.subscribe("$baidu/iot/shadow/mylight/update/accepted",0)
    client.on_message = on_message








