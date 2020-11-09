from django.contrib import admin
from .models import farm, airTempSensor, airTempData
# Register your models here.

admin.site.register(farm)
admin.site.register(airTempSensor)
admin.site.register(airTempData)


