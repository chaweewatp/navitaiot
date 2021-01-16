from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

from .models import farm, airTempSensor, scheduleRelay
from myiot.views import sendCommandOff, sendCommandOn, sendCommandONLED, sendCommandOffLED


import pyrebase
config = {
  "apiKey": "AIzaSyCs9xyouIlR_7SBQwCpL_Bde22ZDC4vpWM",
  "authDomain": "navitaiot.firebaseapp.com",
  "databaseURL": "https://navitaiot.firebaseio.com",
  "storageBucket": "navitaiot.appspot.com",
}

firebase = pyrebase.initialize_app(config)

from myFarm import schedulejobs
from apscheduler.schedulers.background import BackgroundScheduler


# Create your views here.

def home(request):
    print('User access to home page')
    return render(request, 'myFarm/home.html')

def pageFarm(request, id):
    print('User access to myFarm page')
    serverTime=datetime.timestamp(datetime.now())
    print(serverTime)

    db = firebase.database()

    relay1Period1Ref= db.child("farmCode/" + id + "/Relay1/Schedule/Period1").get()
    relay1Ref=db.child("farmCode/" + id + "/Relay1").get()
    print(relay1Ref.val())

    context={
        'farmName' : farm.objects.get(farmCode=id).farmName,
        'farmCode' : farm.objects.get(farmCode=id).farmCode,
        'serverTime': serverTime,
        'initialchk11':relay1Ref.val()['Schedule']['Period1']['pause'],
        'initialchk12': relay1Ref.val()['Schedule']['Period2']['pause'],
        'initialchk13': relay1Ref.val()['Schedule']['Period3']['pause'],
        'initialchk14': relay1Ref.val()['Schedule']['Period4']['pause'],
        'initialchk15': relay1Ref.val()['Schedule']['Period5']['pause'],
        'initialchk16': relay1Ref.val()['Schedule']['Period6']['pause'],

    }

    if (request.method == "POST"):
        command = request.POST.get("command")
        print(command)
        if (command == "ON"):
            print("get command ON")
            sendCommandONLED()
        elif (command == "OFF"):
            print("get command OFF")
            sendCommandOffLED()
        else:
            print("get command N/A")

        return redirect(pageFarm, id='AA0001')

    return render(request, 'myFarm/farm.html', context)



def updateFirebase(request, farmID, text):
    # https://github.com/thisbejim/Pyrebase
    db = firebase.database()
    # db.child("farmCode").child("AA0001").update({"flow1Status": False})
    db.child("farmCode").child(farmID).update(text)
    return HttpResponse("OK")



# schedule added, updated and removed here




