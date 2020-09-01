from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    print('Here we are')
    return HttpResponse('here we are', content_type='text/plain')
