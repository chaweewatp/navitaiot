# from . import mqtt
import paho.mqtt.client as mqtt
import json
import time
import requests
import pyrebase
from datetime import datetime

## firebase configuration
config = {
    "apiKey": "AIzaSyCs9xyouIlR_7SBQwCpL_Bde22ZDC4vpWM",
    "authDomain": "navitaiot.firebaseapp.com",
    "databaseURL": "https://navitaiot.firebaseio.com",
    "storageBucket": "navitaiot.appspot.com",
}

firebase = pyrebase.initialize_app(config)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("TEST/MQTT")
    client.subscribe("reportLED")
    client.subscribe("reportRelay")
    client.subscribe("reportListRelay")
    client.subscribe("wakeUp")
    client.subscribe("TestWiFiBoard")


def on_message(client, userdata, msg):
    urlServer = "https://navitaiot.herokuapp.com/"  # "http://127.0.0.1:8000" #"https://pupaplug.herokuapp.com"
    print(msg.topic)
    print(str(msg.payload.decode("utf-8")))
    data = str(msg.payload.decode("utf-8"))
    # print("message topic :")
    # print(msg.topic)
    # print("message data :")
    # print(data)

    if msg.topic=="TestWiFiBoard":
        print('message recieve ' + data)

    if msg.topic == "wakeUp":
        farmID = data.split('/')[0]
        content = data.split('/')[1]
        # print("farm id is ", farmID, ' content is ', content)
        # url =  "http://127.0.0.1:8000/wakeUp/"
        url = "https://navitaiot.herokuapp.com/wakeUp/"

        payload = {
            'farmID': farmID,
        }

        headers = {
            'content-type': "application/json"
        }
        try:
            requests.request("POST", url, data=json.dumps(payload), headers=headers, timeout=5)
        except requests.Timeout:
            # back off and retry
            pass
        except requests.ConnectionError:
            pass

    if msg.topic == "reportLED":
        farmID = data.split('/')[0]
        content = data.split('/')[1]
        # print("farm id is ", farmID, ' content is ', content)
        if content == 'ledOn':
            text = {"LEDstatus": True}
        elif content == 'ledOff':
            text = {"LEDstatus": False}
        else:
            text = {"LEDstatus": "NA"}
        db = firebase.database()
        # db.child("farmCode").child("AA0001").update({"flow1Status": False})
        db.child("farmCode").child(farmID).update(text)

    if msg.topic == "reportListRelay":
        # print("IoT report Relay status")
        farmID = data.split('/')[0]
        content = data.split('/')[1]
        # print("farm id is ", farmID, ' content is ',content)  ##['relay1On', 'relay2Off','relay3On', 'relay4Off','relay5On', 'relay6Off']
        content = content.split(",")
        # print(content)

        # url =  "http://127.0.0.1:8000/reportRelay/"
        url = "https://navitaiot.herokuapp.com/reportRelay/"
        for item in content:

            payload = {
                'farmID': farmID,
                'content': item
            }

            headers = {
                'content-type': "application/json"
            }
            try:
                requests.request("POST", url, data=json.dumps(payload), headers=headers, timeout=5)
            except requests.Timeout:
                # back off and retry
                pass
            except requests.ConnectionError:
                pass
            db = firebase.database()
            recieveTime = datetime.now().strftime("%Y-%m-%d:%H-%M-%S")
            db.child("farmCode").child(farmID).child('logs').child('relay{}'.format(item[5])).child(
                '{}'.format(recieveTime)).set({'type': 'report', 'oper': item[6:]})

            nowTime = datetime.now()
            serverTime = datetime.timestamp(nowTime)
            db.child("farmCode").child(farmID).child('logs').child('relay{}'.format(content[5])).child('history').child(
                nowTime.year).child(nowTime.month).child(nowTime.day).push({'type': 'report', 'oper': content[6:], 't':serverTime})

            if item == 'relay1On':
                text = {'cur_status': True}
                db.child("farmCode").child(farmID).child('Relay1').update(text)
            elif item == 'relay1Off':
                text = {'cur_status': False}
                db.child("farmCode").child(farmID).child('Relay1').update(text)
            elif item == 'relay2On':
                text = {'cur_status': True}
                db.child("farmCode").child(farmID).child('Relay2').update(text)
            elif item == 'relay2Off':
                text = {'cur_status': False}
                db.child("farmCode").child(farmID).child('Relay2').update(text)
            elif item == 'relay3On':
                text = {'cur_status': True}
                db.child("farmCode").child(farmID).child('Relay3').update(text)
            elif item == 'relay3Off':
                text = {'cur_status': False}
                db.child("farmCode").child(farmID).child('Relay3').update(text)
            elif item == 'relay4On':
                text = {'cur_status': True}
                db.child("farmCode").child(farmID).child('Relay4').update(text)
            elif item == 'relay4Off':
                text = {'cur_status': False}
                db.child("farmCode").child(farmID).child('Relay4').update(text)
            elif item == 'relay5On':
                text = {'cur_status': True}
                db.child("farmCode").child(farmID).child('Relay5').update(text)
            elif item == 'relay5Off':
                text = {'cur_status': False}
                db.child("farmCode").child(farmID).child('Relay5').update(text)
            elif item == 'relay6On':
                text = {'cur_status': True}
                db.child("farmCode").child(farmID).child('Relay6').update(text)
            elif item == 'relay6Off':
                text = {'cur_status': False}
                db.child("farmCode").child(farmID).child('Relay6').update(text)
            else:
                # print("text is NA")
                text = {"relaystatus": "NA"}
                db.child("farmCode").child(farmID).update(text)

        serverTime = datetime.timestamp(datetime.now())
        # print(serverTime)
        text = {'last_time': serverTime}
        db.child("farmCode").child(farmID).update(text)

    if msg.topic == "reportRelay":
        # print("IoT report Relay status")
        farmID = data.split('/')[0]
        content = data.split('/')[1]
        # print("farm id is ", farmID, ' content is ', content)

        # url =  "http://127.0.0.1:8000/reportRelay/"
        url = "https://navitaiot.herokuapp.com/reportRelay/"

        payload = {
            'farmID': farmID,
            'content': content
        }

        headers = {
            'content-type': "application/json"
        }
        try:
            requests.request("POST", url, data=json.dumps(payload), headers=headers, timeout=5)
        except requests.Timeout:
            # back off and retry
            pass
        except requests.ConnectionError:
            pass

        db = firebase.database()
        recieveTime = datetime.now().strftime("%Y-%m-%d:%H-%M-%S")

        db.child("farmCode").child(farmID).child('logs').child('relay{}'.format(content[5])).child(
            '{}'.format(recieveTime)).set({'type': 'report', 'oper': content[6:]})
        nowTime = datetime.now()
        serverTime = datetime.timestamp(nowTime)

        db.child("farmCode").child(farmID).child('logs').child('relay{}'.format(content[5])).child('history').child(
            nowTime.year).child(nowTime.month).child(nowTime.day).push(
            {'type': 'report', 'oper': content[6:], 't': serverTime})

        if content == 'relay1On':
            text = {'cur_status': True}
            db.child("farmCode").child(farmID).child('Relay1').update(text)
        elif content == 'relay1Off':
            text = {'cur_status': False}
            db.child("farmCode").child(farmID).child('Relay1').update(text)
        elif content == 'relay2On':
            text = {'cur_status': True}
            db.child("farmCode").child(farmID).child('Relay2').update(text)
        elif content == 'relay2Off':
            text = {'cur_status': False}
            db.child("farmCode").child(farmID).child('Relay2').update(text)
        elif content == 'relay3On':
            text = {'cur_status': True}
            db.child("farmCode").child(farmID).child('Relay3').update(text)
        elif content == 'relay3Off':
            text = {'cur_status': False}
            db.child("farmCode").child(farmID).child('Relay3').update(text)
        elif content == 'relay4On':
            text = {'cur_status': True}
            db.child("farmCode").child(farmID).child('Relay4').update(text)
        elif content == 'relay4Off':
            text = {'cur_status': False}
            db.child("farmCode").child(farmID).child('Relay4').update(text)
        elif content == 'relay5On':
            text = {'cur_status': True}
            db.child("farmCode").child(farmID).child('Relay5').update(text)
        elif content == 'relay5Off':
            text = {'cur_status': False}
            db.child("farmCode").child(farmID).child('Relay5').update(text)
        elif content == 'relay6On':
            text = {'cur_status': True}
            db.child("farmCode").child(farmID).child('Relay6').update(text)
        elif content == 'relay6Off':
            text = {'cur_status': False}
            db.child("farmCode").child(farmID).child('Relay6').update(text)
        else:
            # print("text is NA")
            text = {"relaystatus": "NA"}
            db.child("farmCode").child(farmID).update(text)

        serverTime = datetime.timestamp(datetime.now())
        # print(serverTime)
        text = {'last_time': serverTime}
        db.child("farmCode").child(farmID).update(text)

    # if msg.topic == "TEST/MQTT_old":
    #     # print(data)
    #     farmID = data[0:6]
    #     # print(farmID)
    #     serverTime = datetime.timestamp(datetime.now())
    #     text = {'last_time': serverTime}
    #     db = firebase.database()
    #     db.child("farmCode").child(farmID).update(text)
    #     recieveTime = datetime.now().strftime("%Y-%m-%d:%H-%M-%S")
    #
    #     content = data.split(' ')
    #     dict_a = {"humid": "boardHumi", "temp": "boardTemp",
    #               "flowSen1": "flowSen1", "flowSen2": "flowSen2","flowSen3": "flowSen3",
    #               "airHumid":"airHumid", "airTemp":"airTemp",
    #               "soil1A":"soil1A", "soil2A":"soil2A", "soil3A":"soil3A",
    #               "soil1B": "soil1B", "soil2B": "soil2B", "soil3B": "soil3B"
    #               }
    #     # print({dict_a["{}".format(item.split('=')[0])] :item.split('=')[1] for item in content[1:]})
    #     raw_data = {'farmID': farmID,
    #                 'detail': {dict_a["{}".format(item.split('=')[0])]: item.split('=')[1] for item in content[1:]}}
    #     db = firebase.database()
    #     #value
    #     for key, value in raw_data['detail'].items():
    #         db.child("farmCode").child(raw_data['farmID']).child('sensors').child(key).update(
    #             {'t': serverTime, 'v': value})
    #         db.child("farmCode").child(raw_data['farmID']).child('sensors').child(key).child('history').child(
    #             # '{}'.format(recieveTime)).set({'v': value})

    if msg.topic == "TEST/MQTT":  #report sensors
        farmID = data[0:6]
        nowTime=datetime.now()
        serverTime = datetime.timestamp(nowTime)
        text = {'last_time': serverTime}
        db = firebase.database()
        db.child("farmCode").child(farmID).update(text)
        recieveTime = datetime.now().strftime("%Y-%m-%d:%H-%M-%S")

        content = data.split(' ')
        dict_a = {"humid": "boardHumi", "temp": "boardTemp",
                  "flowSen1": "flowSen1", "flowSen2": "flowSen2","flowSen3": "flowSen3",
                  "airHumid":"airHumid", "airTemp":"airTemp",
                  "soil1A":"soil1A", "soil2A":"soil2A", "soil3A":"soil3A",
                  "soil1B": "soil1B", "soil2B": "soil2B", "soil3B": "soil3B"
                  }
        # print({dict_a["{}".format(item.split('=')[0])] :item.split('=')[1] for item in content[1:]})
        raw_data = {'farmID': farmID,
                    'detail': {dict_a["{}".format(item.split('=')[0])]: item.split('=')[1] for item in content[1:]}}
        db = firebase.database()
        for key, value in raw_data['detail'].items():
            db.child("farmCode").child(raw_data['farmID']).child('sensors').child(key).update(
                {'t': serverTime, 'v': value})
            db.child("farmCode").child(raw_data['farmID']).child('sensors').child(key).child('history2').child(nowTime.year).child(nowTime.month).child(nowTime.day).push({'t': serverTime, 'v': value})


def sendToMQTT(client, userdata, msg):
    # urlServer =  "http://127.0.0.1:8000"
    urlServer = "https://navitaiot.herokuapp.com/"
    chipID = "AA0001"
    mqttTopic = chipID
    url = urlServer
    payload = {
        'text': "helloFromServer",
    }

    headers = {
        'content-type': "application/json"
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    response = response.json()
    # print('response ' + str(response) + '\n')
    # print("-----------------------------------------")

    client.publish(mqttTopic, str(response['return']))






print('start MQTT client')
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("hjjfrnei:hjjfrnei", password='2YTkbiI66pGxct-1sG2r2grx2yT7sAXj')
client.connect("jaguar.rmq.cloudamqp.com", 1883, 60)
client.loop_start()
print('MQTT client started')

# from django_apscheduler.jobstores import DjangoJobStore
# from django_apscheduler.models import DjangoJobExecution
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
# scheduler.add_jobstore(DjangoJobStore(), "default")
scheduler.start()

# from .foo import foo
# foo()






