from django.contrib import admin
from .models import farm, airTempSensor, airTempData, scheduleRelay, relayDevice
# Register your models here.

admin.site.register(farm)
admin.site.register(airTempSensor)
admin.site.register(airTempData)
admin.site.register(relayDevice)

admin.site.register(scheduleRelay)

