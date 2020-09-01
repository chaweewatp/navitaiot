from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.test1, name='test1'),
]