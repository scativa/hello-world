# MQTT IIoT
Código para implementar un publicador y lector de MQTT con la librería [Paho](https://www.hivemq.com/article/mqtt-client-library-paho-python/). Trabaja con 
[HiveMQ Public Broker](https://www.mqtt-dashboard.com/) o con un servidor local de _Mosquitto_ en Docker.
__Conda__:mqtt
[Google Drive](https://docs.google.com/document/d/1A3d4QocZgWvJe7LC1RL7jZNMMjFawd0_fb8X6QyJZaY/edit#heading=h.w5esckdkohoy)

## Archivos
- *__/HelloWorld/__*: Escriben y leen números random utilizando _broker.mqttdashboard.com_.
- `publisher.py`: Publica en un broker una cantidad dada de mensajes
- `suscribe.py`: Lee durante un tiempo determinado los mensajes de un broker
- `requirements-mqtt.txt`: Requierimientos para el entorno conda nombrado como `mqtt`

## Entorno Conda
### Python
```
conda create -n mqtt python=3.10.4
conda activate mqtt
pip install -r requirements-mqtt.txt
```
Para el proxy de CNEA
```
pip install --proxy "http://proxy-cac.cnea.gov.ar:1280" -r requirements-mqtt.txt
```

### Node Js
[ChatGPT](https://chat.openai.com/c/b66ec0b5-be72-4029-8d09-85f718ca61c4)

```
conda create -n nodejs-mqtt nodejs
conda activate nodejs-mqtt
npm install mqtt
npm install express
```

## Test
En dos consolas de comandos diferentes ejecutar:
```
conda activate mqtt
python .\publisher.py -b localhost -t prueba_mqtt
```
```
conda activate mqtt
python.exe .\suscribe.py -b localhost -t prueba_mqtt
```
El broker puede cambiarse del local a uno público `-b broker.hivemq.com`. En CNEA es filtrado por el proxy. Ver el testeo utilizado para el broker mosquitto que es compatible y complementario a este.

También se puede ver desde un browser a la dirección `http://localhost:3000/consultar-topico/prueba_mqtt/`

Se está intentando insertar el resultado dentro de un archivo html utilizando un javascrip (ver ./http-server) pero está funcionando

## Brokers
### Local
Container `mosquitto-broker`. Ver subcarpeta _mosquitto_

### broker.mqttdashboard.com

usr: __ppca.cnea@gmail.com__
pwd: __gadolinio198MQTT__

https://console.hivemq.cloud/clusters/free/439ac68051274ff18ade34b7bdcee2a1

https://console.hivemq.cloud/

439ac68051274ff18ade34b7bdcee2a1.s1.eu.hivemq.cloud
Port 8883
Websocket Port 8884

Host:	broker.hivemq.com
TCP Port:	1883
Websocket Port:	8000
TLS TCP Port:	8883
TLS Websocket Port:	8884

## Referencias

[MQTT Beginners Guide - Medium.com](https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjI1MmZjYjk3ZGY1YjZiNGY2ZDFhODg1ZjFlNjNkYzRhOWNkMjMwYzUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2MDk5NDc3MzAsImF1ZCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjEwNDIxMDM1MzI0OTMxNjg4NjM4MyIsImVtYWlsIjoic2NhdGl2YUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXpwIjoiMjE2Mjk2MDM1ODM0LWsxazZxZTA2MHMydHAyYTJqYW00bGpkY21zMDBzdHRnLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwibmFtZSI6IlNlYmFzdGnDoW4gQ2F0aXZhIFRvbG9zYSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQU9oMTRHZ04zeUUyT1U4S0VCWUowMjNRQ2E2ZXdSSUNYM2hWeWRURzVQSmdxYzQ9czk2LWMiLCJnaXZlbl9uYW1lIjoiU2ViYXN0acOhbiIsImZhbWlseV9uYW1lIjoiQ2F0aXZhIFRvbG9zYSIsImlhdCI6MTYwOTk0ODAzMCwiZXhwIjoxNjA5OTUxNjMwLCJqdGkiOiIxODFkOTE3YzNkMWZkNGY0MWMxYzYxMmQ3Mjg5M2FlZGRmOTg2MTNjIn0.1oeFwbWMUf4Yw9RfLnPN_Mw_zOdZeTVOJhJjBjF9wB5B3deJQhimPlUzFReJYm2OHJr355hxVdNWy6djV1rQkGibvJTPitNGmfz8prUwlorQQqzhXPvGcOEJezb4CDnZy44WYgq8gnlZ-xNsW6l7UAvpPlCRr0AHkJjGhEJ7lYaALL2PGh0X2Ym2ehrTwg6g9VLmcGyHsYLNau7JEN2F3FXbgDbS1khfji600YNZgNLmvhnH8vrqrDYJvk4Ia0-cOiTftPIFbE0ely4rwHJ61-rf5-YOLahdK9RnFNhDh-M-snIpcMQhuCqm88CXrqIAGbd_nm3kQVllsGZxSUWO9w)

[http://www.mqtt-dashboard.com/](http://www.mqtt-dashboard.com/)

[Node-RED Cookbook](https://cookbook.nodered.org/#mqtt)

[Connect to an MQTT Broker](https://www.infoworld.com/article/2972143/real-time-protocols-for-iot-apps.html)

[Ejemplos Node-RED y MQTT](https://aprendiendoarduino.wordpress.com/2020/03/09/ejemplos-node-red-y-mqtt/)

[Know your real-time protocols for IoT apps](https://www.infoworld.com/article/2972143/real-time-protocols-for-iot-apps.html)
