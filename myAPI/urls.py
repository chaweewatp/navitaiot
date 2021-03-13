from django.urls import path, include
from . import views


urlpatterns = [
    path('login', views.login, name='login'),
    path('test', views.test, name='test'),
    path('createJobSchedule/', views.createJobSchedule, name='createJobSchedule'),
    path('getUser', views.getUser, name='getUser'),

]