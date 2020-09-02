from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def home(request):
    print('Hello world')
    return render(request, 'myiot/home.html')

@csrf_exempt
def testReport(request):
    print('Raw Data: "%s"' % request.__dict__)
    print('Body Data: "%s"' % request.body)
    return HttpResponse("OK")

@csrf_exempt
def testControl(request):
    print(request.headers())
    print('Raw Data: "%s"' % request.__dict__)
    print('Body Data: "%s"' % request.body)
    return HttpResponse("OK")
