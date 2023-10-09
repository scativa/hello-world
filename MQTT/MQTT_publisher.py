import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

mqttBroker ="broker.mqttdashboard.com"
CliendID = "testDIALcam"
Topic = "CameraAnalisis"

client = mqtt.Client(CliendID)
client.connect(mqttBroker) 

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish(Topic, randNumber)
    print("Just published " + str(randNumber) + " to topic " + Topic)
    time.sleep(1)
    
