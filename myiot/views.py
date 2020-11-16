from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

import paho.mqtt.client as mqtt

# from .mqtt import client, sendToMQTT
from .__init__ import client



# Create your views here.


# def home(request):
#     print('Hello world')
#     return render(request, 'myiot/home.html')
#
@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def testAPI(request):
    print('Raw Data: "%s"' % request.__dict__)
    print('Body Data: "%s"' % request.body)
    return Response("OK")
#
# @csrf_exempt
# def testControl(request):
#     print('Raw Data: "%s"' % request.__dict__)
#     print('Body Data: "%s"' % request.body)
#     return HttpResponse("OK")

def sendCommandONLED():
    userdata="blankUser"
    msg="blankMsg"
    chipID="AA0001"
    topic=chipID
    msg="turnONLED"


    # client = mqtt.Client()
    # client.username_pw_set("hjjfrnei:hjjfrnei", password='2YTkbiI66pGxct-1sG2r2grx2yT7sAXj')
    # client.connect("jaguar.rmq.cloudamqp.com", 1883, 60)
    
    client.publish(topic,msg)
    print('Message publish to '+ chipID + ", msg :" +msg)
    print()
    # return HttpResponse("ON")

def sendCommandOffLED():
    userdata = "blankUser"
    msg = "blankMsg"
    chipID = "AA0001"
    topic = chipID
    msg = "turnOffLED"
    # client = mqtt.Client()
    # client.username_pw_set("hjjfrnei:hjjfrnei", password='2YTkbiI66pGxct-1sG2r2grx2yT7sAXj')
    # client.connect("jaguar.rmq.cloudamqp.com", 1883, 60)

    client.publish(topic, msg)
    print('Message publish to ' + chipID + ", msg :" + msg)
    print()
    # return HttpResponse("Off")

def on_message(client, userdata, msg):
    urlServer =  "https://navitaiot.herokuapp.com/"  # "http://127.0.0.1:8000" #"https://pupaplug.herokuapp.com"
    print(msg.topic)