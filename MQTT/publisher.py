# python publisher.py -b localhost -t prueba_mqtt

import paho.mqtt.client as mqtt 
import random
import string
import time
import argparse

ap = argparse.ArgumentParser("MQTT publisher")
ap.add_argument("-b", "--broker", required=False, help="IP o dirección (default 127.0.0.1)")
ap.add_argument("-t", "--topic", required=True, help="Topic")
ap.add_argument("-c", "--client_id", required=False, help="Id del cliente (default random)")
ap.add_argument("-m", "--cant_msg", required=False, help="Cantidad de mensajes a enviar (default 10)")
args = vars(ap.parse_args())

mqttBroker ="127.0.0.1" # "broker.hivemq.com" 
if args['broker'] != None:
    mqttBroker = args['broker']

topic = args['topic']

if args['client_id'] != None:
    client_id = args['client_id']
else:
    client_id = 'Client_{}'.format(''.join(random.choice(string.ascii_lowercase) for i in range(8))) # (random 8 letras minúsculas)

cant_msg = 10
if args['cant_msg'] != None:
    cant_msg = int(args['cant_msg'])

client = mqtt.Client(client_id)
client.connect(mqttBroker) 


while True:
    # Genera un mensaje incremental
    msg=random.randint(0,100)
    msg = f"{msg:03d}"
    
    # y lo publica
    client.publish(topic, msg)

    print("Publicando: ",topic, msg)

    # Espera un tiempo
    time.sleep(0.9)
    
