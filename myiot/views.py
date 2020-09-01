from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    print ('Raw Data: "%s"' % request.body)
    return HttpResponse("OK")
