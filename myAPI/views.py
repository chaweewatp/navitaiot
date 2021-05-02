from django.shortcuts import render
from django.http import HttpResponse
from django.db import close_old_connections

from django_apscheduler.models import DjangoJob

from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)


from rest_framework.authtoken.models import Token
from myAPI.authentication import token_expire_handler
from django.contrib.auth import authenticate
from myAPI.serializers import UserSigninSerializer


from myFarm.models import scheduleRelay, relayDevice, farm

import json

# from .mqtt import client, sendToMQTT
from myiot.__init__ import client
# from navitaiot.__init__ import client

from apscheduler.schedulers.background import BackgroundScheduler
from myiot.__init__ import scheduler
# from navitaiot.__init__ import scheduler

from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.models import DjangoJobExecution

import datetime


from myFarm.models import scheduleRelay, relayDevice, farm
from myiot.views import sendScheduleToIoT, responseSchedule

import pyrebase
config = {
  "apiKey": "AIzaSyCs9xyouIlR_7SBQwCpL_Bde22ZDC4vpWM",
  "authDomain": "navitaiot.firebaseapp.com",
  "databaseURL": "https://navitaiot.firebaseio.com",
  "storageBucket": "navitaiot.appspot.com",
}
firebase = pyrebase.initialize_app(config)

# Create your views here.

@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def test(request):
    return Response("Test")

@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def login(request):
    '''
        This function generate token for a user after authentication success.
        '''
    print('function : login')
    try:
        signin_serializer = UserSigninSerializer(data=request.data)
        if not signin_serializer.is_valid():
            return Response(signin_serializer.errors, status=HTTP_400_BAD_REQUEST)
        user = authenticate(
            username=signin_serializer.data['username'],
            password=signin_serializer.data['password']
        )
        if not user:
            return Response({'detail': 'Invalid Credentials or activate account'}, status=HTTP_404_NOT_FOUND)
        # TOKEN STUFF
        token, _ = Token.objects.get_or_create(user=user)
        # token_expire_handler will check, if the token is expired it will generate new one
        is_expired, token = token_expire_handler(token)  # The implementation will be described further
        # master_log.objects.create(ml_type='login', ml_create_timestamp=timezone.now(), user_id=user)
        print('login success')
        return Response({
            'token': token.key,
            'name':'Miss Jingjai Sawasdee',
            'APIkey':"AIzaSyCs9xyouIlR_7SBQwCpL_Bde22ZDC4vpWM"},
            status.HTTP_200_OK)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def createJobSchedule(request):
    print("function createJobSchedule")
    data = json.loads(str(request.body, encoding='utf-8'))
    try:
        user = Token.objects.get(key=data['token']).user
        for item in farm.objects.filter(farmUser=user):
            if item.farmCode==data["farmCode"]:
                farmCode = data["farmCode"]
                device = data["detail"]["device"]
                duration = data["detail"]["duration"]
                start_hour = data["detail"]["start_hour"]
                start_minute = data["detail"]["start_minute"]
                start_second = 0
                end_hour = data["detail"]["end_hour"]
                end_minute = data["detail"]["end_minute"]
                end_second = 0
                period = data["detail"]["period"]
                pause = data["detail"]["pause"]
                scheduleID_On = '{}_{}_period{}_On'.format(farmCode, device, period)
                scheduleID_Off = '{}_{}_period{}_Off'.format(farmCode, device, period)
                try:
                    newSch = scheduleRelay.objects.get(scheduleId=scheduleID_On)
                    # print('schedule is exist')
                    newSch.period = period
                    newSch.startTime = '{:02d}:{:02d}:{:02d}'.format(int(start_hour), int(start_minute),int(start_second))
                    newSch.duration = duration
                    newSch.dayOfWeek = 'x'
                    newSch.enable = not pause
                    newSch.save()
                except:
                    # print('create new schedule')
                    f1 = farm.objects.get(farmCode=farmCode)
                    r1 = relayDevice.objects.get(farm_id=f1, relayNumber=device[-1])
                    newSch = scheduleRelay(relay=r1, period=period, startTime='{:02d}:{:02d}:{:02d}'.format(int(start_hour), int(start_minute),int(start_second)),
                                           duration=duration,
                                           dayOfWeek='x', enable=True, scheduleId=scheduleID_On)
                    newSch.save()

                jobId = str(newSch.scheduleId)
                text = '{' + '"command":"On","farmID":"{}","device":"{}", "duration":"{}"'.format(farmCode, device, duration) + '}'
                try:
                    scheduler.reschedule_job(jobId, trigger=CronTrigger(
                                      day_of_week='mon,tue,wed,thu,fri,sat,sun', hour=start_hour,minute=start_minute, second=start_second
                                  ))
                    # print('jobs reschedule')
                except:
                    # print('no job existed')
                    # print('create new job')

                    scheduler.add_job(sendScheduleToIoT,
                                      trigger=CronTrigger(
                                          day_of_week='mon,tue,wed,thu,fri,sat,sun', hour=start_hour,minute=start_minute, second=start_second
                                      ),
                                      id=jobId, replace_existing=True, args=[text], max_instances=1,misfire_grace_time=3600)
                DjangoJobExecution.objects.filter(job=jobId).delete()

                # print("Schedule created {}".format(text))
                if pause == False:
                    scheduler.resume_job(jobId)
                    # print("Schedule resume {}".format(text))
                else:
                    scheduler.pause_job(jobId)
                    # print("Schedule pause {}".format(text))

                #update to firebase
                text = {'sch_duration':duration, "sch_on": "{:02d}:{:02d}:{:02d}".format(int(start_hour), int(start_minute), int(start_second)),  "pause":pause}
                db = firebase.database()
                db.child("farmCode").child(farmCode).child('Relay'+str(device[-1])).child('Schedule').child('Period'+str(period)).update(text)

                # off time
                try:
                    newSch = scheduleRelay.objects.get(scheduleId=scheduleID_Off)
                    # print('schedule is exist')
                    newSch.period = period
                    newSch.startTime = '{:02d}:{:02d}:{:02d}'.format(int(end_hour), int(end_minute), int(end_second))
                    newSch.duration = 0
                    newSch.dayOfWeek = 'x'
                    newSch.enable = not pause
                    newSch.save()

                except:
                    # print('create new schedule')
                    f1 = farm.objects.get(farmCode=farmCode)
                    r1 = relayDevice.objects.get(farm_id=f1, relayNumber=device[-1])
                    newSch = scheduleRelay(relay=r1, period=period, startTime='{:02d}:{:02d}:{:02d}'.format(int(end_hour), int(end_minute), int(end_second)), duration=0,
                                           dayOfWeek='x', enable=True, scheduleId=scheduleID_Off)
                    newSch.save()

                jobId = str(newSch.scheduleId)
                text = '{' + '"command":"Off","farmID":"{}","device":"{}"'.format(farmCode, device) + '}'
                try:
                    scheduler.reschedule_job(jobId, trigger=CronTrigger(
                                      day_of_week='mon,tue,wed,thu,fri,sat,sun', hour=end_hour, minute=end_minute,second=end_second
                                  ))

                    # print('jobs reschedule')
                except:
                    # print('no job existed')
                    # print('create new job')

                    scheduler.add_job(sendScheduleToIoT,
                                      trigger=CronTrigger(
                                          day_of_week='mon,tue,wed,thu,fri,sat,sun', hour=end_hour, minute=end_minute,second=end_second
                                      ),
                                      id=jobId, replace_existing=True, args=[text], max_instances=1, misfire_grace_time=3600)
                DjangoJobExecution.objects.filter(job=jobId).delete()
                # print("Schedule created {}".format(text))
                if pause == False:
                    scheduler.resume_job(jobId)
                    # print("Schedule resume {}".format(text))
                else:
                    scheduler.pause_job(jobId)
                    # print("Schedule pause {}".format(text))

                #update to firebase
                text = {"sch_off": "{:02d}:{:02d}:{:02d}".format(int(end_hour), int(end_minute), int(end_second)), "pause":pause}
                # print(str(text)+ " update to firebase")
                db = firebase.database()
                db.child("farmCode").child(farmCode).child('Relay'+str(device[-1])).child('Schedule').child('Period'+str(period)).update(text)

                close_old_connections()
                # ถ้าเลยเวลาเปิดแล้วให้เปิดอัตโนมัติ
                f1 = farm.objects.get(farmCode=farmCode)
                r1 = relayDevice.objects.get(farm_id=f1, relayNumber=device[-1])
                responseSchedule(farmCode, r1)
                return Response({"method":"scheduleSet", "detail":{"device":device,}},status.HTTP_200_OK)
        # else:
        #     return Response({"no farm data"}, status.HTTP_404_NOT_FOUND)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def getUser(request):
    print("function createSchedule")
    data = json.loads(str(request.body, encoding='utf-8'))
    # print(data['token'])
    user = Token.objects.get(key=data['token']).user
    # print(user.__dict__)
    list_farm=farm.objects.filter(farmUser=user)
    # print(list_farm)
    return Response({"token":data['token'], "detail":{"user":user.username, "farm":[item.farmCode for item in list_farm]}},status.HTTP_200_OK)

def firebaseModeSet(mode, farmID, relay):
    print("function firebaseModeSet")

    # print(relay)
    text = {'manual': mode}
    db = firebase.database()
    db.child("farmCode").child(farmID).child(relay).update(text)

def modeManualSet(farmID, relay):
    print("function modeManualSet")

    f1 = farm.objects.get(farmCode=farmID)
    r1 = relayDevice.objects.get(farm=f1, relayNumber=relay[-1])
    r1.manualMode = True
    r1.save()
    #pause schedule

    # update firebase
    firebaseModeSet(mode=True, farmID=farmID, relay=relay)
    # print('farmID :{} - relay number : {} set as Manual mode'.format(farmID, relay))

def modeScheduleSet(farmID, relay):
    print("function modeScheduleSet")
    f1 = farm.objects.get(farmCode=farmID)
    r1 = relayDevice.objects.get(farm=f1, relayNumber=relay[-1])
    r1.manualMode = False
    r1.save()
    # resume schedule

    # update firebase
    firebaseModeSet(mode=False, farmID=farmID, relay=relay)
    # print('farmID :{} - relay number : {} set as Schedule mode'.format(farmID, relay))
    # print(r1.__dict__)

    # เช็คก่อนว่าตอนที่กดมา อยู่ในระหว่าง schedule ไหม มีในเวลาที่ตั้งไว้ไหม
    responseSchedule(farmID, r1)

@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def setMode2(request):
    print("function setMode")
    # print('Raw Data: "%s"' % request.__dict__)
    # print('Body Data: "%s"' % request.body)
    data = json.loads(str(request.body, encoding='utf-8'))
    print(data)
    try:
        user = Token.objects.get(key=data['token']).user
        for item in farm.objects.filter(farmUser=user):
            print(item.farmCode)
            if item.farmCode==data["farmCode"]:
                farmCode=data['farmCode']
                if data['method']=="setMode":
                    relay=data['detail']['device']
                    if data['detail']['mode']=="schedule":
                        # set manual mode "False" in relay model
                        modeScheduleSet(farmCode, relay)

                    elif data['detail']['mode']=="manual":
                        # set manual mode "True" in relay model
                        modeManualSet(farmCode, relay)
                    else:
                        pass
                return Response("OK")
        return Response({"no farm data"}, status.HTTP_404_NOT_FOUND)

    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def sendCommandOn(chipID, device):
    print("function sendCommandOn")
    topic = chipID
    msg = device + "/turnOn"
    client.publish(topic, msg)
    print('Message publish to ' + chipID + ", msg :" + msg)

def sendCommandOff(chipID, device):
    print("function sendCommandOff")

    topic = chipID
    msg = device + "/turnOff"
    client.publish(topic, msg)
    print('Message publish to ' + chipID + ", msg :" + msg)

@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def controlRelay(request):
    print("function controlRelay")
    data = json.loads(str(request.body, encoding='utf-8'))
    try:
        user = Token.objects.get(key=data['token']).user

        for item in farm.objects.filter(farmUser=user):
            print(item.farmCode)
            if item.farmCode==data["farmCode"]:
                farmCode = data["farmCode"]
                relay = data["detail"]["device"]
                if data["method"] == "control":
                    if data["detail"]["control"] == "on":
                        sendCommandOn(chipID=farmCode, device='relay'+relay[-1])
                        # set mode --> manual
                        modeManualSet(farmID=farmCode, relay=relay)

                        recieveTime = datetime.datetime.now().strftime("%Y-%m-%d:%H-%M-%S")
                        db = firebase.database()
                        nowTime = datetime.datetime.now()
                        serverTime = datetime.datetime.timestamp(nowTime)
                        db.child("farmCode").child(farmCode).child('logs').child('relay' + relay[-1]).child(
                            'history').child(
                            nowTime.year).child(nowTime.month).child(nowTime.day).push(
                            {'type': 'manual', 'oper': 'On', 't': serverTime})


                    elif data["detail"]["control"] == "off":
                        sendCommandOff(chipID=farmCode, device='relay'+relay[-1])
                        # set mode --> manual
                        modeManualSet(farmID=farmCode, relay=relay)

                        recieveTime = datetime.datetime.now().strftime("%Y-%m-%d:%H-%M-%S")
                        db = firebase.database()
                        nowTime = datetime.datetime.now()
                        serverTime = datetime.datetime.timestamp(nowTime)
                        db.child("farmCode").child(farmCode).child('logs').child('relay'+relay[-1]).child(
                            'history').child(
                            nowTime.year).child(nowTime.month).child(nowTime.day).push({'type': 'manual', 'oper': 'Off', 't': serverTime})

                    else:
                        pass
                return Response("OK2")
        return Response({"no farm data"}, status.HTTP_404_NOT_FOUND)

    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def getHistory(request):
    return Response("OK2")


def convNextruntime(oldTime):
    newTime=oldTime+ datetime.timedelta(hours=7)
    # return "{}/{}/{} {}-{}".format(newTime.day, newTime.month, newTime.year, newTime.hour, newTime.minute)
    return "{}/{}/{} {}:{}".format(newTime.day, newTime.month, newTime.year, newTime.hour, newTime.minute)

@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def getJobs(request):
    print("function getJobs")
    data = json.loads(str(request.body, encoding='utf-8'))
    return_json={'farmCode':data["farmCode"], 'relay':data['relay'],
            'schedule':{'period1':{'On':{},'Off':{}},
                        'period2': {'On': {}, 'Off': {}},
                        'period3': {'On': {}, 'Off': {}},
                        'period4': {'On': {}, 'Off': {}},
                        'period5': {'On': {}, 'Off': {}},
                        'period6': {'On': {}, 'Off': {}},
                        }}
    try:
        user = Token.objects.get(key=data['token']).user
        for item in farm.objects.filter(farmUser=user):
            if item.farmCode==data["farmCode"]:
                for period in ['1','2','3','4','5','6']:
                    print(period)

                    try:
                        jobOn=DjangoJob.objects.get(id='{}_relay{}_period{}_On'.format(data['farmCode'], data['relay'],period))
                        jobOff= DjangoJob.objects.get(id='{}_relay{}_period{}_Off'.format(data['farmCode'], data['relay'], period))
                        print(jobOn)
                        print(jobOn.next_run_time)
                        print(type(jobOn.next_run_time))

                        if jobOn.next_run_time is not None:
                            return_json['schedule']['period{}'.format(period)]['On'].update({'id':jobOn.id, 'next_run':convNextruntime(jobOn.next_run_time)})
                        else:
                            return_json['schedule']['period{}'.format(period)]['On'].update(
                                {'id': jobOn.id, 'next_run': '---------'})
                        if jobOff.next_run_time is not None:
                            return_json['schedule']['period{}'.format(period)]['Off'].update({'id':jobOff.id, 'next_run':convNextruntime(jobOff.next_run_time)})
                        else:
                            return_json['schedule']['period{}'.format(period)]['Off'].update({'id':jobOff.id, 'next_run':'---------'})

                    except:
                        return_json['schedule']['period{}'.format(period)]['On'].update(
                            {'id': 'none', 'next_run': '---------'})
                        return_json['schedule']['period{}'.format(period)]['Off'].update(
                            {'id': 'none', 'next_run': '---------'})

                # for job in scheduler.get_jobs():
                #     print(job.id)
                #     print(job.name)
                #     print(job.next_run_time)
        print(return_json)
        return Response(return_json, status=HTTP_200_OK)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)