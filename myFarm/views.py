from django.shortcuts import render
from django.http import HttpResponse

from .models import farm, airTempSensor
import pyrebase

config = {
  "apiKey": "AIzaSyCs9xyouIlR_7SBQwCpL_Bde22ZDC4vpWM",
  "authDomain": "navitaiot.firebaseapp.com",
  "databaseURL": "https://navitaiot.firebaseio.com",
  "storageBucket": "navitaiot.appspot.com",
}

firebase = pyrebase.initialize_app(config)

# Create your views here.

def home(request):
    print('Hello world')
    return render(request, 'myFarm/home.html')

def pageFarm(request, id):
    print('Hello world')
    context={
        'farmName' : farm.objects.get(farmCode=id).farmName,
        'farmCode' : farm.objects.get(farmCode=id).farmCode
    }
    return render(request, 'myFarm/farm.html', context)


def updateFirebase(request):
    # https://github.com/thisbejim/Pyrebase
    db = firebase.database()
    db.child("farmCode").child("AA0001").update({"flow1Status": False})
    return HttpResponse("OK")

