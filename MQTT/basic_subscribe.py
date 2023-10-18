import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

# mqttBroker ="broker.mqttdashboard.com"
# mqttBroker ="172.31.69.0"
mqttBroker ="192.168.26.71"
CliendID = "cliente"
Topic = "topico3"

client = mqtt.Client(CliendID)
client.connect(mqttBroker) 

client.loop_start()

client.subscribe(Topic)
client.on_message=on_message 

time.sleep(30)
client.loop_stop()
