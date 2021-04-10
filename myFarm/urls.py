from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('myfarm/<id>/', views.pageFarm, name='pageFarm'),
    path('updateFirebase/', views.updateFirebase, name='updateFirebase'),
    path('history/<id>/', views.history, name='history'),
    path('index/', views.index, name='index'),
    path('farm2/<farmCode>', views.farm2, name='farm2'),
    path('history2/<farmCode>/', views.history2, name='history2'),

]