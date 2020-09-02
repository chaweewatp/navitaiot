from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.testReport, name='testReport'),
    path('control/', views.testControl, name="testControl"),
]