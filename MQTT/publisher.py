# python publisher.py -b localhost -t prueba_mqtt

import paho.mqtt.client as mqtt 
import logging
from random import randrange, uniform
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

#format = "%(asctime)s,%(msecs)03d: %(message)s"
format = "%(msecs)03d,%(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt='%H:%M:%S')
inc_msg = 0
msgs = [0] * cant_msg

while True:
    randNumber = uniform(20.0, 21.0)
    msg = "{:02d}".format(inc_msg)
    
    client.publish(topic, msg)
    #logging.info("publisher,{}".format(msg))
    msgs[inc_msg] = (int(round(time.time() * 1000)), msg)

    print(topic, msg)
    # print(f"{msg}) {msgs[inc_msg][0]:03d}") 

    time.sleep(0.9)
    inc_msg += 1
    if inc_msg == cant_msg:
        break
  
# for ms, msg in msgs:
#     print("{:03d},{}".format(ms, msg)) 
