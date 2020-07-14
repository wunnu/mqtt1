import time
import paho.mqtt.client as mqtt
import datetime

#成功发布消息的操作
def on_publish(msg, rc):
    if rc == 0:
        print("publish success, msg = " + msg)

#连接后的操作 0为成功
def on_connect(client, userdata, flags, rc):
    print("Connection returned " + str(rc))

client = mqtt.Client(
    client_id="test_mqtt_sender_1", #client_id
    clean_session=True,
    userdata=None,
    protocol='MQTTv311'
)

trust = "C:/Python27/pom/root_cert.pem" #开启TLS时的认证文件目录
user = "smart-sensor/ldw"
pwd = "O7hrHKUYJLqxwajP/5/2fqdZ8KIDZ/aR4/CWrmRt6Gg="
endpoint = "smart-sensor.mqtt.iot.gz.baidubce.com"
port = 1884
topic = "as"

client.tls_insecure_set(True) #检查hostname的cert认证
client.tls_set(trust) #设置认证文件
client.username_pw_set(user, pwd) #设置用户名，密码
client.connect(endpoint, port, 60) #连接服务 keepalive=60
client.on_connect = on_connect #连接后的操作
client.loop_start()
time.sleep(2)
count = 0
while count < 5: #发布五条消息
    count = count + 1
    msg = str(datetime.datetime.now())
    rc , mid = client.publish(topic, payload=msg, qos=1) #qos
    on_publish(msg, rc)
    time.sleep(2)
