#!/usr/bin/env python

import paho.mqtt.client as mqtt

trust = "C:/Python27/pom/root_cert.pem" #开启TLS时的认证文件目录
user = "smart-sensor/ldw"
pwd = "O7hrHKUYJLqxwajP/5/2fqdZ8KIDZ/aR4/CWrmRt6Gg="
endpoint = "smart-sensor.mqtt.iot.gz.baidubce.com"
port = 1884
topic = "as"

#连接后返回0为成功
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

client.tls_insecure_set(True) #检查hostname的cert认证
client.tls_set(trust) #设置认证文件
client.username_pw_set(user, pwd) #设置用户名，密码
client.on_connect = on_connect #连接后的操作
client.on_message = on_message #接受消息的操作
client.connect(endpoint, port, 60) #连接服务 keepalive=60
client.loop_forever()
