from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('myfarm/<id>/', views.pageFarm, name='pageFarm'),
    path('updateFirebase/', views.updateFirebase, name='updateFirebase'),
    path('history/<id>/', views.history, name='history'),

]