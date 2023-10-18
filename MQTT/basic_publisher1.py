import paho.mqtt.client as mqtt 
from random import randrange
import time

# mqttBroker ="broker.mqttdashboard.com" 
mqttBroker ="localhost" 
CliendID = "cliente"
Topic = "CameraAnalisis"

client = mqtt.Client(CliendID)
client.connect(mqttBroker) 

while True:
    randNumber = randrange(10)
    client.publish(Topic, randNumber)
    print("Just published " + str(randNumber) + " to topic " + Topic)
    time.sleep(1)
    
