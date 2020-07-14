import time
import paho.mqtt.client as mqtt
import datetime

#�ɹ�������Ϣ�Ĳ���
def on_publish(msg, rc):
    if rc == 0:
        print("publish success, msg = " + msg)

#���Ӻ�Ĳ��� 0Ϊ�ɹ�
def on_connect(client, userdata, flags, rc):
    print("Connection returned " + str(rc))

client = mqtt.Client(
    client_id="test_mqtt_sender_1", #client_id
    clean_session=True,
    userdata=None,
    protocol='MQTTv311'
)

trust = "C:/Python27/pom/root_cert.pem" #����TLSʱ����֤�ļ�Ŀ¼
user = "smart-sensor/ldw"
pwd = "O7hrHKUYJLqxwajP/5/2fqdZ8KIDZ/aR4/CWrmRt6Gg="
endpoint = "smart-sensor.mqtt.iot.gz.baidubce.com"
port = 1884
topic = "as"

client.tls_insecure_set(True) #���hostname��cert��֤
client.tls_set(trust) #������֤�ļ�
client.username_pw_set(user, pwd) #�����û���������
client.connect(endpoint, port, 60) #���ӷ��� keepalive=60
client.on_connect = on_connect #���Ӻ�Ĳ���
client.loop_start()
time.sleep(2)
count = 0
while count < 5: #����������Ϣ
    count = count + 1
    msg = str(datetime.datetime.now())
    rc , mid = client.publish(topic, payload=msg, qos=1) #qos
    on_publish(msg, rc)
    time.sleep(2)
