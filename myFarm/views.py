from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import farm
from myiot.views import sendCommandONLED, sendCommandOffLED
from rest_framework.authtoken.models import Token
from myAPI.authentication import token_expire_handler
from django.contrib.auth import authenticate



import pyrebase
config = {
  "apiKey": "AIzaSyCs9xyouIlR_7SBQwCpL_Bde22ZDC4vpWM",
    
  "authDomain": "navitaiot.firebaseapp.com",
  "databaseURL": "https://navitaiot.firebaseio.com",
  "storageBucket": "navitaiot.appspot.com",
}

firebase = pyrebase.initialize_app(config)


# Create your views here.



def index(request):
    return render(request, 'myFarm/index.html')

def home(request):
    print('User access to home page')
    return render(request, 'myFarm/home.html')

def pageFarm(request, id):
    print('User access to myFarm page')
    serverTime=datetime.timestamp(datetime.now())
    print(serverTime)

    db = firebase.database()

    relay1Ref=db.child("farmCode/" + id + "/Relay1").get()
    relay2Ref=db.child("farmCode/" + id + "/Relay2").get()
    relay3Ref=db.child("farmCode/" + id + "/Relay3").get()
    relay4Ref=db.child("farmCode/" + id + "/Relay4").get()
    relay5Ref=db.child("farmCode/" + id + "/Relay5").get()
    relay6Ref=db.child("farmCode/" + id + "/Relay6").get()

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
        'initialchk21': relay2Ref.val()['Schedule']['Period1']['pause'],
        'initialchk22': relay2Ref.val()['Schedule']['Period2']['pause'],
        'initialchk23': relay2Ref.val()['Schedule']['Period3']['pause'],
        'initialchk24': relay2Ref.val()['Schedule']['Period4']['pause'],
        'initialchk25': relay2Ref.val()['Schedule']['Period5']['pause'],
        'initialchk26': relay2Ref.val()['Schedule']['Period6']['pause'],
        'initialchk31': relay3Ref.val()['Schedule']['Period1']['pause'],
        'initialchk32': relay3Ref.val()['Schedule']['Period2']['pause'],
        'initialchk33': relay3Ref.val()['Schedule']['Period3']['pause'],
        'initialchk34': relay3Ref.val()['Schedule']['Period4']['pause'],
        'initialchk35': relay3Ref.val()['Schedule']['Period5']['pause'],
        'initialchk36': relay3Ref.val()['Schedule']['Period6']['pause'],
        'initialchk41': relay4Ref.val()['Schedule']['Period1']['pause'],
        'initialchk42': relay4Ref.val()['Schedule']['Period2']['pause'],
        'initialchk43': relay4Ref.val()['Schedule']['Period3']['pause'],
        'initialchk44': relay4Ref.val()['Schedule']['Period4']['pause'],
        'initialchk45': relay4Ref.val()['Schedule']['Period5']['pause'],
        'initialchk46': relay4Ref.val()['Schedule']['Period6']['pause'],
        'initialchk51': relay5Ref.val()['Schedule']['Period1']['pause'],
        'initialchk52': relay5Ref.val()['Schedule']['Period2']['pause'],
        'initialchk53': relay5Ref.val()['Schedule']['Period3']['pause'],
        'initialchk54': relay5Ref.val()['Schedule']['Period4']['pause'],
        'initialchk55': relay5Ref.val()['Schedule']['Period5']['pause'],
        'initialchk56': relay5Ref.val()['Schedule']['Period6']['pause'],
        'initialchk61': relay6Ref.val()['Schedule']['Period1']['pause'],
        'initialchk62': relay6Ref.val()['Schedule']['Period2']['pause'],
        'initialchk63': relay6Ref.val()['Schedule']['Period3']['pause'],
        'initialchk64': relay6Ref.val()['Schedule']['Period4']['pause'],
        'initialchk65': relay6Ref.val()['Schedule']['Period5']['pause'],
        'initialchk66': relay6Ref.val()['Schedule']['Period6']['pause'],

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

def history(request, id):
    context={
        'farmName': farm.objects.get(farmCode=id).farmName,
        'farmCode': farm.objects.get(farmCode=id).farmCode,
    }
    return render(request, 'myFarm/history.html', context)

def farm2(request, tk, farmCode):
    user = Token.objects.get(key=tk).user
    for item in farm.objects.filter(farmUser=user):
        if item.farmCode==farmCode:
            print('User access to myFarm page' + farmCode)
            serverTime=datetime.timestamp(datetime.now())
            db = firebase.database()
            relay1Ref=db.child("farmCode/" + farmCode + "/Relay1").get()
            relay2Ref=db.child("farmCode/" + farmCode + "/Relay2").get()
            relay3Ref=db.child("farmCode/" + farmCode + "/Relay3").get()
            relay4Ref=db.child("farmCode/" + farmCode + "/Relay4").get()
            relay5Ref=db.child("farmCode/" + farmCode + "/Relay5").get()
            relay6Ref=db.child("farmCode/" + farmCode + "/Relay6").get()

            context={
                'farmName' : farm.objects.get(farmCode=farmCode).farmName,
                'farmCode' : farm.objects.get(farmCode=farmCode).farmCode,
                'serverTime': serverTime,
                'relay1Name':"ปั้มน้ำ",
                'relay2Name': "ปั๊มปุ๋ย",
                'relay3Name': "เดรนวาล์ว",
                'relay4Name': "วาล์วโซน 1",
                'relay5Name': "วาล์วโซน 2",
                'relay6Name': "วาล์วโซน 3",
                'initialchk11':relay1Ref.val()['Schedule']['Period1']['pause'],
                'initialchk12': relay1Ref.val()['Schedule']['Period2']['pause'],
                'initialchk13': relay1Ref.val()['Schedule']['Period3']['pause'],
                'initialchk14': relay1Ref.val()['Schedule']['Period4']['pause'],
                'initialchk15': relay1Ref.val()['Schedule']['Period5']['pause'],
                'initialchk16': relay1Ref.val()['Schedule']['Period6']['pause'],
                'initialchk21': relay2Ref.val()['Schedule']['Period1']['pause'],
                'initialchk22': relay2Ref.val()['Schedule']['Period2']['pause'],
                'initialchk23': relay2Ref.val()['Schedule']['Period3']['pause'],
                'initialchk24': relay2Ref.val()['Schedule']['Period4']['pause'],
                'initialchk25': relay2Ref.val()['Schedule']['Period5']['pause'],
                'initialchk26': relay2Ref.val()['Schedule']['Period6']['pause'],
                'initialchk31': relay3Ref.val()['Schedule']['Period1']['pause'],
                'initialchk32': relay3Ref.val()['Schedule']['Period2']['pause'],
                'initialchk33': relay3Ref.val()['Schedule']['Period3']['pause'],
                'initialchk34': relay3Ref.val()['Schedule']['Period4']['pause'],
                'initialchk35': relay3Ref.val()['Schedule']['Period5']['pause'],
                'initialchk36': relay3Ref.val()['Schedule']['Period6']['pause'],
                'initialchk41': relay4Ref.val()['Schedule']['Period1']['pause'],
                'initialchk42': relay4Ref.val()['Schedule']['Period2']['pause'],
                'initialchk43': relay4Ref.val()['Schedule']['Period3']['pause'],
                'initialchk44': relay4Ref.val()['Schedule']['Period4']['pause'],
                'initialchk45': relay4Ref.val()['Schedule']['Period5']['pause'],
                'initialchk46': relay4Ref.val()['Schedule']['Period6']['pause'],
                'initialchk51': relay5Ref.val()['Schedule']['Period1']['pause'],
                'initialchk52': relay5Ref.val()['Schedule']['Period2']['pause'],
                'initialchk53': relay5Ref.val()['Schedule']['Period3']['pause'],
                'initialchk54': relay5Ref.val()['Schedule']['Period4']['pause'],
                'initialchk55': relay5Ref.val()['Schedule']['Period5']['pause'],
                'initialchk56': relay5Ref.val()['Schedule']['Period6']['pause'],
                'initialchk61': relay6Ref.val()['Schedule']['Period1']['pause'],
                'initialchk62': relay6Ref.val()['Schedule']['Period2']['pause'],
                'initialchk63': relay6Ref.val()['Schedule']['Period3']['pause'],
                'initialchk64': relay6Ref.val()['Schedule']['Period4']['pause'],
                'initialchk65': relay6Ref.val()['Schedule']['Period5']['pause'],
                'initialchk66': relay6Ref.val()['Schedule']['Period6']['pause'],

            }
            print(context)
            return render(request, 'myFarm/farm2.html', context)
    return HttpResponse("No farm")

def history2(request, farmCode):
    context={
        'farmName': farm.objects.get(farmCode=farmCode).farmName,
        'farmCode': farm.objects.get(farmCode=farmCode).farmCode,
    }
    return render(request, 'myFarm/history2.html', context)

def history3(request, tk, farmCode):
    context={
        'farmName': farm.objects.get(farmCode=farmCode).farmName,
        'farmCode': farm.objects.get(farmCode=farmCode).farmCode,
    }
    print(context)
    return render(request, 'myFarm/history3.html', context)

def updateFirebase(request, farmID, text):
    # https://github.com/thisbejim/Pyrebase
    db = firebase.database()
    # db.child("farmCode").child("AA0001").update({"flow1Status": False})
    db.child("farmCode").child(farmID).update(text)
    return HttpResponse("OK")

# schedule added, updated and removed here


def farmlist(request, tk):
    try:
        user = Token.objects.get(key=tk).user
        listFarm=[]
        for item in farm.objects.filter(farmUser=user):
            listFarm.append({'farmCode': item.farmCode, 'lastTime':"10 minutes ago"})


        context={'listFarm':listFarm}
        return render(request, 'myFarm/farmlist.html', context)
    except:
        return HttpResponse("Unauthorization")

