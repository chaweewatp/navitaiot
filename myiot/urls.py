from django.urls import path, include
from . import views

urlpatterns = [
    path('sendCommandONLED/', views.sendCommandONLED, name='sendCommandONLED'),
    path('sendCommandOffLED/', views.sendCommandOffLED, name='sendCommandOffLED'),
    path('testAPI2/', views.testAPI2, name='testAPI2'),
    path('createSchedule/', views.createSchedule, name='createSchedule'),
    path('printSchedule/', views.printSchedule, name='printSchedule'),
    path('removeSchedule/', views.removeSchedule, name='removeSchedule'),
    path('wakeUp/', views.wakeUp, name='wakeUp'),
    path('setMode/', views.setMode, name='setMode'),
    path('emergencyOff/', views.emergencyOff, name='emergencyOff'),
    path('reportRelay/', views.reportRelay, name='reportRelay'),

]