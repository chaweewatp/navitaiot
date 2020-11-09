import paho.mqtt.client as mqtt
import json
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("TEST/MQTT")


def on_message(client, userdata, msg):
    urlServer =  "https://navitaiot.herokuapp.com/"  # "http://127.0.0.1:8000" #"https://pupaplug.herokuapp.com"
    print(msg.topic)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("hjjfrnei:hjjfrnei", password='2YTkbiI66pGxct-1sG2r2grx2yT7sAXj')
client.connect("jaguar.rmq.cloudamqp.com", 1883, 60)

