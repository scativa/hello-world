# python suscribe.py -b localhost -t prueba_mqtt -w 320

import paho.mqtt.client as mqtt
import logging
import time
from random import randrange, uniform
import random
import string
import argparse


msgs = list()

def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    print(f"Recibido: {message.topic}: {msg}")
    if int(msg) > 70:
        print("se calienta el agua del mate")


ap = argparse.ArgumentParser("MQTT publisher")
ap.add_argument("-b", "--broker", required=False, help="IP o dirección (default 127.0.0.1)")
ap.add_argument("-t", "--topic", required=True, help="Topic")
ap.add_argument("-c", "--client_id", required=False, help="Id del cliente (default random)")
ap.add_argument("-w", "--wait_time", required=False, help="Tiempo (seg) de espera de mensajes (default 10 segundos)")
ap.add_argument("-q", "--qos", required=False, help="Calidad de servicio (QOS) {0, 1, 2} (default 2)")
args = vars(ap.parse_args())

mqttBroker ="127.0.0.1" # "broker.hivemq.com" 
if args['broker'] != None:
    mqttBroker = args['broker']

topic = args['topic']

if args['client_id'] != None:
    client_id = args['client_id']
else:
    client_id = 'Client_{}'.format(''.join(random.choice(string.ascii_lowercase) for i in range(8))) # (random 8 letras minúsculas)

wait_time = 10
if args['wait_time'] != None:
    cant_msg = args['wait_time']

QOS = 2
if args['qos'] != None:
    cant_msg = args['qos']

client = mqtt.Client(client_id)
client.connect(mqttBroker) 

client.subscribe(topic, qos=QOS)
client.on_message=on_message 

client.loop_start()
print("listening topic {}...".format(topic))
# client.loop_forever()
while True:
    time.sleep(wait_time) # tiempo durante el cual va a estar escuchando

client.loop_stop()
print("stop listening.")

