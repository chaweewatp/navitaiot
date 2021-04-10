from django.urls import path, include
from . import views


urlpatterns = [
    path('login', views.login, name='login'),
    path('test', views.test, name='test'),
    path('getUser', views.getUser, name='getUser'),
    path('setMode2/', views.setMode2, name='setMode2'),
    path('controlRelay/', views.controlRelay, name='controlRelay'),
    path('createJobSchedule/', views.createJobSchedule, name='createJobSchedule'),
]