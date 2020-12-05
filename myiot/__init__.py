# from . import mqtt
import paho.mqtt.client as mqtt
import json
import time
import requests
import pyrebase


## firebase configuration
config = {
  "apiKey": "AIzaSyCs9xyouIlR_7SBQwCpL_Bde22ZDC4vpWM",
  "authDomain": "navitaiot.firebaseapp.com",
  "databaseURL": "https://navitaiot.firebaseio.com",
  "storageBucket": "navitaiot.appspot.com",
}

firebase = pyrebase.initialize_app(config)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("TEST/MQTT")
    client.subscribe("reportLED")
    client.subscribe("reportRelay")



def on_message(client, userdata, msg):
    urlServer =  "https://navitaiot.herokuapp.com/"  # "http://127.0.0.1:8000" #"https://pupaplug.herokuapp.com"
    # print(msg.topic)
    # print(str(msg.payload.decode("utf-8")))
    data=str(msg.payload.decode("utf-8"))
    if msg.topic == "reportLED":
        farmID=data.split('/')[0]
        content=data.split('/')[1]
        print("farm id is ", farmID, ' content is ', content)
        if content == 'ledOn':
            text={"LEDstatus":True}
        elif content == 'ledOff':
            text = {"LEDstatus": False}
        else:
            text={"LEDstatus": "NA"}
        db = firebase.database()
        # db.child("farmCode").child("AA0001").update({"flow1Status": False})
        db.child("farmCode").child(farmID).update(text)

    if msg.topic == "reportRelay":
        print("IoT report Relay status")

        farmID=data.split('/')[0]
        content=data.split('/')[1]
        print("farm id is ", farmID, ' content is ', content)

        if content == 'relay1On':
            text={"relay1On":True}
        elif content == 'relay1Off':
            text = {"relay1On": False}
        elif content == 'relay2On':
            text = {"relay2On": True}
        elif content == 'relay2Off':
            text = {"relay2On": False}
        elif content == 'relay3On':
            text = {"relay3On": True}
        elif content == 'relay3Off':
            text = {"relay3On": False}
        elif content == 'relay4On':
            text = {"relay4On": True}
        elif content == 'relay4Off':
            text = {"relay4On": False}
        elif content == 'relay5On':
            text = {"relay5On": True}
        elif content == 'relay5Off':
            text = {"relay5On": False}
        elif content == 'relay6On':
            text = {"relay6On": True}
        elif content == 'relay6Off':
            text = {"relay6On": False}
        else:
            print("text is NA")
            text={"relaystatus": "NA"}
        db = firebase.database()
        # db.child("farmCode").child("AA0001").update({"flow1Status": False})
        db.child("farmCode").child(farmID).update(text)



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


print('start MQTT client')
client.loop_start()
print('MQTT client started')

