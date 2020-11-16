from django.urls import path, include
from . import views

urlpatterns = [
    path('sendCommandONLED/', views.sendCommandONLED, name='sendCommandONLED'),
    path('sendCommandOffLED/', views.sendCommandOffLED, name='sendCommandOffLED'),
    path('testAPI/', views.testAPI, name='testAPI'),

]