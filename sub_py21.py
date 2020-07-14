#!/usr/bin/env python

import paho.mqtt.client as mqtt

trust = "C:/Python27/pom/root_cert.pem" #����TLSʱ����֤�ļ�Ŀ¼
user = "smart-sensor/ldw"
pwd = "O7hrHKUYJLqxwajP/5/2fqdZ8KIDZ/aR4/CWrmRt6Gg="
endpoint = "smart-sensor.mqtt.iot.gz.baidubce.com"
port = 1884
topic = "as"

#���Ӻ󷵻�0Ϊ�ɹ�
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic, qos=1) #qos

def on_message(client, userdata, msg):
    print("topic:"+msg.topic+" Message:"+str(msg.payload))
    
client = mqtt.Client(
    client_id="test_mqtt_receiver_1",
    clean_session=True,
    userdata=None,
    protocol='MQTTv31'
)

client.tls_insecure_set(True) #���hostname��cert��֤
client.tls_set(trust) #������֤�ļ�
client.username_pw_set(user, pwd) #�����û���������
client.on_connect = on_connect #���Ӻ�Ĳ���
client.on_message = on_message #������Ϣ�Ĳ���
client.connect(endpoint, port, 60) #���ӷ��� keepalive=60
client.loop_forever()
