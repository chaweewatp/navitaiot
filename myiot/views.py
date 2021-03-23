from django.http import HttpResponse
from django.db import close_old_connections

import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework.renderers import JSONRenderer

# from .mqtt import client, sendToMQTT
from .__init__ import client

from apscheduler.schedulers.background import BackgroundScheduler
from .__init__ import scheduler

from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.models import DjangoJobExecution

import datetime


from myFarm.models import scheduleRelay, relayDevice, farm

# firebase config
import pyrebase
config = {
  "apiKey": "AIzaSyCs9xyouIlR_7SBQwCpL_Bde22ZDC4vpWM",
  "authDomain": "navitaiot.firebaseapp.com",
  "databaseURL": "https://navitaiot.firebaseio.com",
  "storageBucket": "navitaiot.appspot.com",
}
firebase = pyrebase.initialize_app(config)



# Create your views here.


# def home(request):
#     print('Hello world')
#     return render(request, 'myiot/home.html')
#



@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def testAPI(request):
    print("function testAPI")

    # print('Raw Data: "%s"' % request.__dict__)
    # print('Body Data: "%s"' % request.body)
    return Response("OK")


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


def responseSchedule(farmID, r1):
    print("function responseSchedule")

    onSchedule=False
    for period in [1,2,3,4,5,6]:
        # print(period)
        try:
            on_schedule=scheduleRelay.objects.get(scheduleId='{}_relay{}_period{}_On'.format(r1.farm.farmCode, r1.relayNumber,period))
            # print(on_schedule.__dict__)
            if  (on_schedule.enable):
                on_time = datetime.time(int(on_schedule.startTime.split(':')[0]),
                                        int(on_schedule.startTime.split(':')[1]),
                                        int(on_schedule.startTime.split(':')[2]))
                off_schedule=scheduleRelay.objects.get(scheduleId='{}_relay{}_period{}_Off'.format(r1.farm.farmCode, r1.relayNumber,period))
                off_time=datetime.time(int(off_schedule.startTime.split(':')[0]), int(off_schedule.startTime.split(':')[1]), int(off_schedule.startTime.split(':')[2]))

                current_time = datetime.datetime.now().time()
                check=check_time(current_time,on_time,off_time)
                print(check)
                if (check):
                    onSchedule=True
        except:
            pass

    print(onSchedule)
    #send command to NbIoT
    if (onSchedule):
        r1.scheduleStatus=True
        r1.save()
        if r1.manualMode==False:
            sendCommandOn(farmID, 'relay'+r1.relayNumber)
            print('Send command to IoT')
            recieveTime = datetime.datetime.now().strftime("%Y-%m-%d:%H-%M-%S")
            db = firebase.database()
            db.child("farmCode").child(farmID).child('logs').child('relay'+str(r1.relayNumber)).child(
                '{}'.format(recieveTime)).set({'type': 'schedule', 'oper': 'On'})

        text = {'sch_status':True}
        db = firebase.database()
        db.child("farmCode").child(farmID).child('Relay' + str(r1.relayNumber)).update(text)
    else:
        r1.scheduleStatus=False
        r1.save()
        if r1.manualMode==False:
            sendCommandOff(farmID, 'relay'+r1.relayNumber)
            recieveTime = datetime.datetime.now().strftime("%Y-%m-%d:%H-%M-%S")
            db = firebase.database()
            db.child("farmCode").child(farmID).child('logs').child('relay'+str(r1.relayNumber)).child(
                '{}'.format(recieveTime)).set({'type': 'schedule', 'oper': 'Off'})
        text = {'sch_status':False}
        db = firebase.database()
        db.child("farmCode").child(farmID).child('Relay' + str(r1.relayNumber)).update(text)



def modeScheduleSet(farmID, relay):
    print("function modeScheduleSet")
    f1 = farm.objects.get(farmCode=farmID)
    r1 = relayDevice.objects.get(farm=f1, relayNumber=relay[-1])
    r1.manualMode = False
    r1.save()
    #resume schedule

    # update firebase
    firebaseModeSet(mode=False, farmID=farmID, relay=relay)
    # print('farmID :{} - relay number : {} set as Schedule mode'.format(farmID, relay))
    # print(r1.__dict__)

    # เช็คก่อนว่าตอนที่กดมา อยู่ในระหว่าง schedule ไหม มีในเวลาที่ตั้งไว้ไหม
    responseSchedule(farmID, r1)
    # onSchedule=False
    # for period in [1,2,3,4,5,6]:
    #     # print(period)
    #     try:
    #         on_schedule=scheduleRelay.objects.get(scheduleId='{}_relay{}_period{}_On'.format(r1.farm.farmCode, r1.relayNumber,period))
    #         # print(on_schedule.__dict__)
    #         if  (on_schedule.enable):
    #             on_time = datetime.time(int(on_schedule.startTime.split(':')[0]),
    #                                     int(on_schedule.startTime.split(':')[1]),
    #                                     int(on_schedule.startTime.split(':')[2]))
    #             off_schedule=scheduleRelay.objects.get(scheduleId='{}_relay{}_period{}_Off'.format(r1.farm.farmCode, r1.relayNumber,period))
    #             off_time=datetime.time(int(off_schedule.startTime.split(':')[0]), int(off_schedule.startTime.split(':')[1]), int(off_schedule.startTime.split(':')[2]))
    #
    #             current_time = datetime.datetime.now().time()
    #             check=check_time(current_time,on_time,off_time)
    #             print(check)
    #             if (check):
    #                 onSchedule=True
    #     except:
    #         pass
    #
    # print(onSchedule)
    # #send command to NbIoT
    # if (onSchedule):
    #     r1.scheduleStatus=True
    #     r1.save()
    #     sendCommandOn(farmID, 'relay'+relay[-1])
    #
    #     text = {'sch_status':True}
    #     db = firebase.database()
    #     db.child("farmCode").child(farmID).child('Relay' + str(r1.relayNumber)).update(text)
    # else:
    #     r1.scheduleStatus=False
    #     r1.save()
    #     sendCommandOff(farmID, 'relay'+relay[-1])
    #     text = {'sch_status':False}
    #     db = firebase.database()
    #     db.child("farmCode").child(farmID).child('Relay' + str(r1.relayNumber)).update(text)



@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def setMode(request):
    print("function setMode")

    # print('Raw Data: "%s"' % request.__dict__)
    # print('Body Data: "%s"' % request.body)
    data = json.loads(str(request.body, encoding='utf-8'))
    farmID=data['farmID']
    if data['method']=="setMode":
        relay=data['detail']['device']
        if data['detail']['mode']=="schedule":
            # set manual mode "False" in relay model
            modeScheduleSet(farmID, relay)

        elif data['detail']['mode']=="manual":
            # set manual mode "True" in relay model
            modeManualSet(farmID, relay)
        else:
            pass



    return Response("OK")


def updateFirebase(request, farmID, text):
    print("function updateFirebase")

    # https://github.com/thisbejim/Pyrebase
    db = firebase.database()
    # db.child("farmCode").child("AA0001").update({"flow1Status": False})
    db.child("farmCode").child(farmID).update(text)
    return HttpResponse("OK")

#
# @csrf_exempt
# def testControl(request):
#     print('Raw Data: "%s"' % request.__dict__)
#     print('Body Data: "%s"' % request.body)
#     return HttpResponse("OK")

def sendCommandONLED():
    print("function sendCommandONLED")

    userdata = "blankUser"
    msg = "blankMsg"
    chipID = "AA0001"
    topic = chipID
    msg = "turnONLED"

    # client = mqtt.Client()
    # client.username_pw_set("hjjfrnei:hjjfrnei", password='2YTkbiI66pGxct-1sG2r2grx2yT7sAXj')
    # client.connect("jaguar.rmq.cloudamqp.com", 1883, 60)

    client.publish(topic, msg)
    # print('Message publish to ' + chipID + ", msg :" + msg)
    # print()
    # return HttpResponse("ON")


def sendCommandOffLED():
    print("function sendCommandOffLED")

    userdata = "blankUser"
    msg = "blankMsg"
    chipID = "AA0001"
    topic = chipID
    msg = "turnOffLED"
    # client = mqtt.Client()
    # client.username_pw_set("hjjfrnei:hjjfrnei", password='2YTkbiI66pGxct-1sG2r2grx2yT7sAXj')
    # client.connect("jaguar.rmq.cloudamqp.com", 1883, 60)

    client.publish(topic, msg)
    # print('Message publish to ' + chipID + ", msg :" + msg)
    # print()
    # return HttpResponse("Off")


# def on_message(client, userdata, msg):
#     urlServer =  "https://navitaiot.herokuapp.com/"  # "http://127.0.0.1:8000" #"https://pupaplug.herokuapp.com"
#     print(msg.topic)


def sendCommandOff(chipID, device):
    print("function sendCommandOff")

    topic = chipID
    msg = device + "/turnOff"
    client.publish(topic, msg)
    print('Message publish to ' + chipID + ", msg :" + msg)

def sendCommandOn(chipID, device):
    print("function sendCommandOn")
    topic = chipID
    msg = device + "/turnOn"
    client.publish(topic, msg)
    print('Message publish to ' + chipID + ", msg :" + msg)





@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def testAPI2(request):
    print("function testAPI2")

    # print('Raw Data: "%s"' % request.__dict__)
    # print('Body Data: "%s"' % request.body)
    data = json.loads(str(request.body, encoding='utf-8'))
    # print(data)
    # print(data["method"])

    chipID = data["farmID"]
    relay = data["detail"]["device"]
    if data["method"] == "control":
        if data["detail"]["control"] == "on":
            sendCommandOn(chipID=chipID, device='relay'+relay[-1])
            # set mode --> manual
            modeManualSet(farmID=chipID, relay=relay)

            recieveTime = datetime.datetime.now().strftime("%Y-%m-%d:%H-%M-%S")
            db = firebase.database()
            db.child("farmCode").child(chipID).child('logs').child('relay'+relay[-1]).child(
                '{}'.format(recieveTime)).set({'type': 'manual', 'oper': 'On'})

        elif data["detail"]["control"] == "off":
            sendCommandOff(chipID=chipID, device='relay'+relay[-1])
            # set mode --> manual
            modeManualSet(farmID=chipID, relay=relay)

            recieveTime = datetime.datetime.now().strftime("%Y-%m-%d:%H-%M-%S")
            db = firebase.database()
            db.child("farmCode").child(chipID).child('logs').child('relay'+relay[-1]).child(
                '{}'.format(recieveTime)).set({'type': 'manual', 'oper': 'Off'})

        else:
            pass
    return Response("OK2")



def sendScheduleToIoT(text):
    print("function sendScheduleToIoT")

    """ send set of command to IoT"""
    print(text)
    res = json.loads(text)
    print(res)
    chipId = res["farmID"]
    device = res["device"]
    f1 = farm.objects.get(farmCode=chipId)
    r1 = relayDevice.objects.get(farm=f1, relayNumber=device[-1])
    print('relay detail :')
    print(r1.__dict__)
    print('relay manual mode :')
    print(r1.manualMode)
    if res["command"] == "On":
        if r1.manualMode == False: #check if manual mode is disable
            sendCommandOn(chipID=chipId, device=device)
            print('Send command to IoT')
            recieveTime = datetime.datetime.now().strftime("%Y-%m-%d:%H-%M-%S")
            db = firebase.database()
            db.child("farmCode").child(chipId).child('logs').child('relay'+device[-1]).child(
                '{}'.format(recieveTime)).set({'type': 'schedule', 'oper': 'on'})
        r1.scheduleStatus=True
        r1.save()
        text = {'sch_status':True}
        db = firebase.database()
        db.child("farmCode").child(chipId).child('Relay' + str(device[-1])).update(text)

    elif res["command"] == "Off":
        if r1.manualMode == False:  #check if manual mode is disable
            sendCommandOff(chipID=chipId, device=device)
            print('Send command to IoT')
            recieveTime = datetime.datetime.now().strftime("%Y-%m-%d:%H-%M-%S")
            db = firebase.database()
            db.child("farmCode").child(chipId).child('logs').child('relay'+device[-1]).child(
                '{}'.format(recieveTime)).set({'type': 'schedule', 'oper': 'off'})



        r1.scheduleStatus=False
        r1.save()
        text = {'sch_status':False}
        db = firebase.database()
        db.child("farmCode").child(chipId).child('Relay' + str(device[-1])).update(text)

    else:
        print('Relay was set to manual')


# def sendCommandOnTest(text):
#     # print(text)
#     topic = "AA0001"
#     msg = "relay3" + "/turnOn"
#     client.publish(topic, msg)
#     # print('Message publish to ' + "AA0001" + ", msg :" + msg)


def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def createSchedule(request):
    print("function createSchedule")
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

    # on time
    try:
        newSch = scheduleRelay.objects.get(scheduleId=scheduleID_On)
        print('schedule is exist')
        newSch.period = period
        newSch.startTime = '{:02d}:{:02d}:{:02d}'.format(int(start_hour), int(start_minute),int(start_second))
        newSch.duration = duration
        newSch.dayOfWeek = 'x'
        newSch.enable = not pause
        newSch.save()
    except:
        print('create new schedule')
        f1 = farm.objects.get(farmCode=farmID)
        r1 = relayDevice.objects.get(farm_id=f1, relayNumber=device[-1])
        newSch = scheduleRelay(relay=r1, period=period, startTime='{:02d}:{:02d}:{:02d}'.format(int(start_hour), int(start_minute),int(start_second)),
                               duration=duration,
                               dayOfWeek='x', enable=True, scheduleId=scheduleID_On)
        newSch.save()

    jobId = str(newSch.scheduleId)

    # delete previous jobExecutions
    jobs = DjangoJobExecution.objects.filter(job_id=jobId)
    if len(jobs) > 1:
        for item in jobs:
            item.delete()

    # scheduler = BackgroundScheduler()
    # scheduler=BlockingScheduler(timezone=settings.TIME_ZONE)
    # scheduler.add_jobstore(DjangoJobStore(), "default")

    text = '{' + '"command":"On","farmID":"{}","device":"{}", "duration":"{}"'.format(farmID, device, duration) + '}'
    try:
        scheduler.reschedule_job(jobId, trigger=CronTrigger(
                          day_of_week='mon,tue,wed,thu,fri,sat,sun', hour=start_hour,minute=start_minute, second=start_second
                      ))
        print('jobs reschedule')
    except:
        print('no job existed')
        print('create new job')

        scheduler.add_job(sendScheduleToIoT,
                          trigger=CronTrigger(
                              day_of_week='mon,tue,wed,thu,fri,sat,sun', hour=start_hour,minute=start_minute, second=start_second
                          ),
                          id=jobId, replace_existing=True, args=[text], max_instances=1,misfire_grace_time=3600)
    # scheduler.add_job(
    #     delete_old_job_executions,
    #     trigger=CronTrigger(
    #         day_of_week='mon,tue,wed,thu,fri,sat,sun', hour="00", minute="00"
    #     ),  # Midnight on Monday, before start of the next work week.
    #     id="delete_old_job_executions",
    #     max_instances=1,
    #     replace_existing=True, jitter=3
    # )
    # scheduler.start()

    print("Schedule created {}".format(text))
    if pause == False:
        scheduler.resume_job(jobId)
        print("Schedule resume {}".format(text))
    else:
        scheduler.pause_job(jobId)
        print("Schedule pause {}".format(text))

    #update to firebase

    text = {'sch_duration':duration, "sch_on": "{:02d}:{:02d}:{:02d}".format(int(start_hour), int(start_minute), int(start_second)),  "pause":pause}

    print(str(text)+ " update to firebase")
    db = firebase.database()
    db.child("farmCode").child(farmID).child('Relay'+str(device[-1])).child('Schedule').child('Period'+str(period)).update(text)

    # off time
    try:
        newSch = scheduleRelay.objects.get(scheduleId=scheduleID_Off)
        print('schedule is exist')
        newSch.period = period
        newSch.startTime = '{:02d}:{:02d}:{:02d}'.format(int(end_hour), int(end_minute), int(end_second))
        newSch.duration = 0
        newSch.dayOfWeek = 'x'
        newSch.enable = not pause
        newSch.save()

    except:
        print('create new schedule')
        f1 = farm.objects.get(farmCode=farmID)
        r1 = relayDevice.objects.get(farm_id=f1, relayNumber=device[-1])
        newSch = scheduleRelay(relay=r1, period=period, startTime='{:02d}:{:02d}:{:02d}'.format(int(end_hour), int(end_minute), int(end_second)), duration=0,
                               dayOfWeek='x', enable=True, scheduleId=scheduleID_Off)
        newSch.save()

    jobId = str(newSch.scheduleId)

    # delete previous jobExecutions
    jobs = DjangoJobExecution.objects.filter(job_id=jobId)
    if len(jobs) > 1:
        for item in jobs:
            item.delete()

    # scheduler = BackgroundScheduler()
    # scheduler=BlockingScheduler(timezone=settings.TIME_ZONE)
    # scheduler.add_jobstore(DjangoJobStore(), "default")
    text = '{' + '"command":"Off","farmID":"{}","device":"{}"'.format(farmID, device) + '}'
    try:
        #if scheduler is exist, then reschedule job
        scheduler.reschedule_job(jobId, trigger=CronTrigger(
                          day_of_week='mon,tue,wed,thu,fri,sat,sun', hour=end_hour, minute=end_minute,second=end_second
                      ))
        print('jobs reschedule')
    except:
        print('no job existed')
        print('create new job')

        scheduler.add_job(sendScheduleToIoT,
                          trigger=CronTrigger(
                              day_of_week='mon,tue,wed,thu,fri,sat,sun', hour=end_hour, minute=end_minute,second=end_second
                          ),
                          id=jobId, replace_existing=True, args=[text], max_instances=1, misfire_grace_time=3600)
    # scheduler.add_job(
    #     delete_old_job_executions,
    #     trigger=CronTrigger(
    #         day_of_week='mon,tue,wed,thu,fri,sat,sun', hour="00", minute="00"
    #     ),  # Midnight on Monday, before start of the next work week.
    #     id="delete_old_job_executions",
    #     max_instances=1,
    #     replace_existing=True, jitter=3
    # )

    # scheduler.start()

    print("Schedule created {}".format(text))
    if pause == False:
        scheduler.resume_job(jobId)
        print("Schedule resume {}".format(text))
    else:
        scheduler.pause_job(jobId)
        print("Schedule pause {}".format(text))

    #update to firebase
    text = {"sch_off": "{:02d}:{:02d}:{:02d}".format(int(end_hour), int(end_minute), int(end_second)), "pause":pause}
    print(str(text)+ " update to firebase")
    db = firebase.database()
    db.child("farmCode").child(farmID).child('Relay'+str(device[-1])).child('Schedule').child('Period'+str(period)).update(text)

    close_old_connections()

    # ถ้าเลยเวลาเปิดแล้วให้เปิดอัตโนมัติ
    f1 = farm.objects.get(farmCode=farmID)
    r1 = relayDevice.objects.get(farm_id=f1, relayNumber=device[-1])
    responseSchedule(farmID, r1)
    return Response("OK")


def check_time(time_to_check, on_time, off_time):
    if time_to_check > on_time and time_to_check < off_time:
        return True
    else:
        return False


@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def removeSchedule(request):
    print("function removeSchedule")

    data = json.loads(str(request.body, encoding='utf-8'))
    farmID = data["farmID"]
    device = data["detail"]["device"]
    scheduler = BackgroundScheduler()
    scheduler.remove_job('{}_{}'.format(farmID, device))
    return Response("OK")


# @api_view(['POST'])
# @permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
# def printSchedule(request):
#     scheduler = BackgroundScheduler()
#     scheduler.print_jobs()
#     print(scheduler.get_jobs())
#     print(scheduler.get_job('AA0001_relay1'))
#     return Response("OK")


@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def wakeUp(request):
    print("function wakeUp")

    data = json.loads(str(request.body, encoding='utf-8'))
    print(data)
    farmID = data["farmID"]
    f1 = farm.objects.get(farmCode=farmID)
    relay_list = relayDevice.objects.filter(farm=f1)
    relay_num = []
    command = []
    for item in relay_list:
        relay_num.append(item.relayNumber)
        if item.manualMode==True:
            command.append(False)
        else:
            command.append(item.scheduleStatus)


    command = ['turnOn' if item is True else 'turnOff' for item in command]

    topic = "{}/getCurrentCommand".format(farmID)
    # msg = "relay" + relay_num[0] + s/' + command[0] + ",relay" + relay_num[1] + '/' + command[1] + ",relay" + relay_num[
    #     2] + '/' + command[2]

    msg=JSONRenderer().render({"relay{}".format(relay_num[0]):"{}".format(command[0]),
                               "relay{}".format(relay_num[1]):"{}".format(command[1]),
                               "relay{}".format(relay_num[2]):"{}".format(command[2]),
                               "relay{}".format(relay_num[3]):"{}".format(command[3]),
                               "relay{}".format(relay_num[4]):"{}".format(command[4]),
                               "relay{}".format(relay_num[5]):"{}".format(command[5])})
    print(msg)
    print(str(msg))
    client.publish(topic, msg)
    print('Message publish to ' + "{}".format(farmID) + ", msg :" + str(msg))

    return Response("OK")




@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def emergencyOff(request):
    print("function emergenctOff")

    data = json.loads(str(request.body, encoding='utf-8'))
    print(data)
    farmID = data["farmID"]
    f1 = farm.objects.get(farmCode=farmID)
    relay_list = relayDevice.objects.filter(farm=f1)
    relay_num = []
    command = []
    for item in relay_list:
        relay_num.append(item.relayNumber)
    json_data={"relay{}".format(item):"turnOff" for item in relay_num}
    print(json_data)
    topic = "{}/getCurrentCommand".format(farmID)
    msg = JSONRenderer().render(json_data)
    # msg=JSONRenderer().render({"relay{}".format(relay_num[0]):"turnOff",
    #                            "relay{}".format(relay_num[1]):"turnOff",
    #                            "relay{}".format(relay_num[2]):"turnOff",
    #                            "relay{}".format(relay_num[3]):"turnOff",
    #                            "relay{}".format(relay_num[4]):"turnOff",
    #                            "relay{}".format(relay_num[5]):"turnOff"})
    print(msg)
    print(str(msg))
    client.publish(topic, msg)
    print('Message publish to ' + "{}".format(farmID) + ", msg :" + str(msg))
    for item in relay_list:
        print(item.__dict__)
        item.manualMode=True
        item.save()
        print(item.__dict__)
        firebaseModeSet(mode=True, farmID=farmID, relay="Relay{}".format(item.relayNumber))

    return Response("OK")





@api_view(['POST'])
@permission_classes((AllowAny,))  # here we specify permission by default we set IsAuthenticated
def reportRelay(request):
    print("function reportRelay")
    data = json.loads(str(request.body, encoding='utf-8'))
    print(data)
    farmID = data["farmID"]
    content=data['content']
    f1 = farm.objects.get(farmCode=farmID)
    r1= relayDevice.objects.get(farm=f1, relayNumber=content[5])
    if content[6:]=="On":
        r1.currentStatus=True
        r1.save()
    elif content[6:]=="Off":
        r1.currentStatus=False
        r1.save()

    return Response("OK")


def updateRTDB(request):
    print("function updateRTDB")

    serverTime=datetime.datetime.now().strftime("%Y-%m-%d:%H-%M-%S")
    timeStamp=datetime.datetime.timestamp(datetime.datetime.now())

    print(serverTime)

    raw_data={'farmID':'AA0001','detail':{'boardHumi':60.9,'boardTemp':34,'flowSen1':False}}
    db = firebase.database()
    for key, value in raw_data['detail'].items():
        print(key)
        print(value)
        db.child("farmCode").child(raw_data['farmID']).child('sensors').child(key).update({'t':timeStamp, 'v':value})
        db.child("farmCode").child(raw_data['farmID']).child('sensors').child(key).child('history').update({'{}'.format(serverTime):value})

    return HttpResponse("OK")

def returnJob(request):
    print("function returnJob")
    print(scheduler.get_jobs())
    for item in scheduler.get_jobs():
        print(item.id)
        print(item.name)
        print(item.next_run_time)

    return HttpResponse("OK")

def getJob(request, id):
    print("function getJob")

    # id="AA0001_relay6_period1_Off"
    sch=scheduler.get_job(job_id=id)
    print(sch)

    return HttpResponse("OK")


def removeJob(request,id):
    print("function removeJob")
    scheduler.remove_job(job_id=id)
    return HttpResponse("OK")


