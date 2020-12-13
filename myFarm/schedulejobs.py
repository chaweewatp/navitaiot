from datetime import datetime
import os
from .models import scheduleRelay
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

def getScheduleID():
    return 'AA0001_relay1'


def updateSchedule():
    scheduleID=getScheduleID()
    try:
        new_schedule=scheduleRelay.objects.get(scheduleId=scheduleID)
        new_schedule.duration = 200
        new_schedule.dayOfWeek = "sun, mon, tue, wed, thu, fri, sat"
        new_schedule.enable = True
        new_schedule.save()
        print("saving...{}".format(new_schedule.__dict__))
    except :
        print('schedule not found')


def sendScheduleToIoT(text):
    """ send set of command to IoT"""
    print(text)
    print('Send command to IoT')


def start():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(updateSchedule, 'interval', minutes=1)
    scheduler.add_job(sendScheduleToIoT, 'cron', day_of_week='mon, tue, wed, thu, fri, sat, sun', hour=11, minute=59, args=["{'farmID':'AA0001','device':'relay1'}"])
    scheduler.start()

