from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

import paho.mqtt.client as mqtt

# from .mqtt import client, sendToMQTT
from .__init__ import client

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from myFarm.models import scheduleRelay, relayDevice, farm


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
    userdata = "blankUser"
    msg = "blankMsg"
    chipID = "AA0001"
    topic = chipID
    msg = "turnONLED"

    # client = mqtt.Client()
    # client.username_pw_set("hjjfrnei:hjjfrnei", password='2YTkbiI66pGxct-1sG2r2grx2yT7sAXj')
    # client.connect("jaguar.rmq.cloudamqp.com", 1883, 60)

    client.publish(topic, msg)
    print('Message publish to ' + chipID + ", msg :" + msg)
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


# def on_message(client, userdata, msg):
#     urlServer =  "https://navitaiot.herokuapp.com/"  # "http://127.0.0.1:8000" #"https://pupaplug.herokuapp.com"
#     print(msg.topic)


def sendCommandOff(chipID, device):
    topic = chipID
    msg = device + "/turnOff"
    client.publish(topic, msg)
    print('Message publish to ' + chipID + ", msg :" + msg)


def sendCommandOn(chipID, device):
    topic = chipID
    msg = device + "/turnOn"
    client.publish(topic, msg)
    print('Message publish to ' + chipID + ", msg :" + msg)


@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def testAPI2(request):
    print('Raw Data: "%s"' % request.__dict__)
    print('Body Data: "%s"' % request.body)
    data = json.loads(str(request.body, encoding='utf-8'))
    # print(data)
    # print(data["method"])

    chipID = data["farmID"]
    device = data["detail"]["device"]
    if data["method"] == "control":
        if data["detail"]["control"] == "on":
            sendCommandOn(chipID=chipID, device=device)
        elif data["detail"]["control"] == "off":
            sendCommandOff(chipID=chipID, device=device)
        else:
            pass
    return Response("OK2")


def sendCommandOnDuration(chipID, device, duration):
    topic = chipID + "/turnOnDuration/"
    msg = device + str(duration)
    client.publish(topic, msg)
    print('Message publish to ' + chipID + ", msg :" + msg)


def sendScheduleToIoT(text):
    """ send set of command to IoT"""
    print(text)
    res = json.loads(text)
    print(res)
    if res["command"] == "On":
        # chipId="AA0001"
        # device="relay1"
        # duration=20000
        chipId = res["farmID"]
        device = res["device"]
        duration = res["duration"]
        # sendCommandOnDuration(chipID=chipId, device=device, duration=duration)
        sendCommandOn(chipID=chipId, device=device)
        print('Send command to IoT')
    elif res["command"] == "Off":
        # chipId="AA0001"
        # device="relay1"
        chipId = res["farmID"]
        device = res["device"]
        duration = 20000
        sendCommandOff(chipID=chipId, device=device)
        print('Send command to IoT')


def sendCommandOnTest(text):
    print(text)
    topic = "AA0001"
    msg = "relay3" + "/turnOn"
    client.publish(topic, msg)
    print('Message publish to ' + "AA0001" + ", msg :" + msg)


def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def createSchedule(request):
    data = json.loads(str(request.body, encoding='utf-8'))
    print(data)
    farmID = data["farmID"]
    device = data["detail"]["device"]
    duration = data["detail"]["duration"]
    start_hour = data["detail"]["start_hour"]
    start_minute = data["detail"]["start_minute"]
    start_second = data["detail"]["start_second"]
    end_hour = data["detail"]["end_hour"]
    end_minute = data["detail"]["end_minute"]
    end_second = data["detail"]["end_second"]

    period = data["detail"]["period"]
    pause = data["detail"]["pause"]
    scheduleID_On = '{}_{}_period{}_On'.format(farmID, device, period)
    scheduleID_Off = '{}_{}_period{}_Off'.format(farmID, device, period)

    try:
        newSch = scheduleRelay.objects.get(scheduleId=scheduleID_On)
        print('schedule is exist')
        newSch.period = period
        newSch.startTime = '{}:{}'.format(start_hour, start_minute)
        newSch.duration = duration
        newSch.dayOfWeek = 'x'
        newSch.enable = True
        newSch.save()

    except:
        print('create new schedule')
        f1 = farm.objects.get(farmCode=farmID)
        r1 = relayDevice.objects.get(farm_id=f1, relayNumber=device[-1])
        newSch = scheduleRelay(relay=r1, period=period, startTime='{}:{}'.format(start_hour, start_minute),
                               duration=duration,
                               dayOfWeek='x', enable=True, scheduleId=scheduleID_On)
        newSch.save()

    jobId = str(newSch.scheduleId)
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    text = '{' + '"command":"On","farmID":"{}","device":"{}", "duration":"{}"'.format(farmID, device, duration) + '}'
    # scheduler.add_job(updateSchedule, 'interval', minutes=1)
    # scheduler.add_job(sendCommandOnTest, 'cron', id=jobId, replace_existing=True, day_of_week='mon, tue, wed, thu, fri, sat, sun', hour=hour, minute=minute, args=["{'farmID':'AA0001','device':'relay1'}"])
    # scheduler.add_job(sendCommandOnTest, trigger=CronTrigger(day_of_week='mon,tue,wed,thu,fri,sat,sun', hour=hour, minute=minute),
    #                   id=jobId, replace_existing=True, args=[text])
    scheduler.add_job(sendScheduleToIoT, trigger=CronTrigger(day_of_week='mon,tue,wed,thu,fri,sat,sun', hour=start_hour,
                                                             minute=start_minute), second=start_second,
                      id=jobId, replace_existing=True, args=[text], misfire_grace_time=3600)
    scheduler.start()
    print("Schedule created {}".format(text))

    if pause == False:
        scheduler.resume_job(jobId)
        print("Schedule resume {}".format(text))
    else:
        scheduler.pause_job(jobId)
        print("Schedule pause {}".format(text))

    try:
        newSch = scheduleRelay.objects.get(scheduleId=scheduleID_Off)
        print('schedule is exist')
        newSch.period = period
        newSch.startTime = '{}:{}'.format(end_hour, end_hour)
        newSch.duration = 0
        newSch.dayOfWeek = 'x'
        newSch.enable = True
        newSch.save()

    except:
        print('create new schedule')
        f1 = farm.objects.get(farmCode=farmID)
        r1 = relayDevice.objects.get(farm_id=f1, relayNumber=device[-1])
        newSch = scheduleRelay(relay=r1, period=period, startTime='{}:{}'.format(end_hour, end_minute), duration=0,
                               dayOfWeek='x', enable=True, scheduleId=scheduleID_Off)
        newSch.save()

    jobId = str(newSch.scheduleId)
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    text = '{' + '"command":"Off","farmID":"{}","device":"{}"'.format(farmID, device) + '}'
    # scheduler.add_job(updateSchedule, 'interval', minutes=1)
    # scheduler.add_job(sendCommandOnTest, 'cron', id=jobId, replace_existing=True, day_of_week='mon, tue, wed, thu, fri, sat, sun', hour=hour, minute=minute, args=["{'farmID':'AA0001','device':'relay1'}"])
    # scheduler.add_job(sendCommandOnTest, trigger=CronTrigger(day_of_week='mon,tue,wed,thu,fri,sat,sun', hour=hour, minute=minute),
    #                   id=jobId, replace_existing=True, args=[text])
    scheduler.add_job(sendScheduleToIoT,
                      trigger=CronTrigger(day_of_week='mon,tue,wed,thu,fri,sat,sun', hour=end_hour, minute=end_minute,
                                          second=end_second, ),
                      id=jobId, replace_existing=True, args=[text], misfire_grace_time=3600)
    scheduler.start()
    print("Schedule created {}".format(text))
    if pause == False:
        scheduler.resume_job(jobId)
        print("Schedule resume {}".format(text))

    else:
        scheduler.pause_job(jobId)
        print("Schedule pause {}".format(text))

    return Response("OK")


@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def removeSchedule(request):
    data = json.loads(str(request.body, encoding='utf-8'))
    farmID = data["farmID"]
    device = data["detail"]["device"]
    scheduler = BackgroundScheduler()
    scheduler.remove_job('{}_{}'.format(farmID, device))
    return Response("OK")


@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def printSchedule(request):
    scheduler = BackgroundScheduler()
    scheduler.print_jobs()
    print(scheduler.get_jobs())
    print(scheduler.get_job('AA0001_relay1'))
    return Response("OK")


@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def wakeUp(request):
    data = json.loads(str(request.body, encoding='utf-8'))
    print(data)
    farmID = data["farmID"]
    f1 = farm.objects.get(farmCode=farmID)
    relay_list = relayDevice.objects.filter(farm=f1)
    relay_num = []
    command = []
    for item in relay_list:
        relay_num.append(item.relayNumber)
        command.append(item.scheduleStatus)

    command = ['turnOn' if item is True else 'turnOff' for item in command]

    topic = "AA0001/getCurrentCommand"
    msg = "relay" + relay_num[0] + '/' + command[0] + ",relay" + relay_num[1] + '/' + command[1] + ",relay" + relay_num[
        2] + '/' + command[2]
    client.publish(topic, msg)
    print('Message publish to ' + "AA0001" + ", msg :" + msg)

    return Response("OK")
