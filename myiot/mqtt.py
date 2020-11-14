import paho.mqtt.client as mqtt
import json
import time
import requests

def on_connect(client, userdata, flags, rc):


    print("Connected with result code "+str(rc))
    client.subscribe("TEST/MQTT")


def on_message(client, userdata, msg):
    urlServer =  "https://navitaiot.herokuapp.com/"  # "http://127.0.0.1:8000" #"https://pupaplug.herokuapp.com"
    print(msg.topic)
    print(str(msg.payload.decode("utf-8")))




def sendToMQTT(client, userdata, msg):
    # urlServer =  "http://127.0.0.1:8000"
    urlServer =  "https://navitaiot.herokuapp.com/"

    chipID="AA0001"
    mqttTopic=chipID
    url = urlServer

    payload = {
        'text': "helloFromServer",
    }

    headers = {
        'content-type': "application/json"
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    response = response.json()
    print('response ' + str(response) + '\n')
    print("-----------------------------------------")

    client.publish(mqttTopic, str(response['return']))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.username_pw_set("hjjfrnei:hjjfrnei", password='2YTkbiI66pGxct-1sG2r2grx2yT7sAXj')
client.connect("jaguar.rmq.cloudamqp.com", 1883, 60)

