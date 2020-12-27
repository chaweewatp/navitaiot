from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
valveType=[('1','drain valve'),
           ('2','zone valve')]


class farm(models.Model):
    farmName = models.CharField(max_length=255)
    farmCode = models.CharField(max_length=255)
    # farmUser = models.ForeignKey(User, on_delete=models.CASCADE)  # relation
    class Meta:
        ordering = ['farmName']
    def __str__(self):
        return "{}-{}".format(self.id, self.farmName)


class zone(models.Model):
    farm = models.ForeignKey(farm, on_delete=models.CASCADE)
    zoneNumber = models.CharField(max_length=10)
    class Meta:
        ordering = ['id']
    def __str__(self):
        return "{}-{}".format(self.id, self.farm)


class soilHumidSensor(models.Model):
    farm = models.ForeignKey(farm, on_delete=models.CASCADE)
    sensorNumber = models.CharField(max_length=10)

    class Meta:
        ordering = ['farm', 'sensorNumber']
    def __str__(self):
        return "{}-{}-{}".format(self.id, self.farm, self.sensorNumber)


class boardHumidSensor(models.Model):
    farm = models.ForeignKey(farm, on_delete=models.CASCADE)
    sensorNumber = models.CharField(max_length=10)

    class Meta:
        ordering = ['farm', 'sensorNumber']
    def __str__(self):
        return "{}-{}-{}".format(self.id, self.farm, self.sensorNumber)

class boardTempSensor(models.Model):
    farm = models.ForeignKey(farm, on_delete=models.CASCADE)
    sensorNumber = models.CharField(max_length=10)
    class Meta:
        ordering = ['farm', 'sensorNumber']
    def __str__(self):
        return "{}-{}-{}".format(self.id, self.farm, self.sensorNumber)



class airHumidSensor(models.Model):
    farm = models.ForeignKey(farm, on_delete=models.CASCADE)
    sensorNumber = models.CharField(max_length=10)

    class Meta:
        ordering = ['farm', 'sensorNumber']
    def __str__(self):
        return "{}-{}-{}".format(self.id, self.farm, self.sensorNumber)

class airTempSensor(models.Model):
    farm = models.ForeignKey(farm, on_delete=models.CASCADE)
    sensorNumber = models.CharField(max_length=10)
    class Meta:
        ordering = ['farm', 'sensorNumber']
    def __str__(self):
        return "{}-{}-{}".format(self.id, self.farm, self.sensorNumber)


class flowSensor(models.Model):
    farm = models.ForeignKey(farm, on_delete=models.CASCADE)
    sensorNumber = models.CharField(max_length=10)
    class Meta:
        ordering = ['farm', 'sensorNumber']
    def __str__(self):
        return "{}-{}-{}".format(self.id, self.farm, self.sensorNumber)

class flowData(models.Model):
    sensor = models.ForeignKey(flowSensor, on_delete=models.CASCADE)
    data=models.BooleanField(default=False)
    dataCreated = models.DateTimeField(default = datetime.now)
    def __str__(self):
        return "{}-{}".format(self.id, self.sensor)

class airHumidData(models.Model):
    sensor = models.ForeignKey(airHumidSensor, on_delete=models.CASCADE)
    data=models.FloatField(max_length=255)
    dataCreated = models.DateTimeField(default = datetime.now)
    def __str__(self):
        return "{}-{}".format(self.id, self.sensor)

class airTempData(models.Model):
    sensor = models.ForeignKey(airTempSensor, on_delete=models.CASCADE)
    data=models.FloatField(max_length=255)
    dataCreated = models.DateTimeField(default = datetime.now)
    def __str__(self):
        return "{}-{}".format(self.id, self.sensor)


class soilHumidData(models.Model):
    sensor = models.ForeignKey(soilHumidSensor, on_delete=models.CASCADE)
    data=models.FloatField(max_length=255)
    dataCreated = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return "{}-{}".format(self.id, self.sensor)


class boardHumidData(models.Model):
    sensor = models.ForeignKey(boardHumidSensor, on_delete=models.CASCADE)
    data=models.FloatField(max_length=255)
    dataCreated = models.DateTimeField(default = datetime.now)
    def __str__(self):
        return "{}-{}".format(self.id, self.sensor)

class boardTempData(models.Model):
    sensor = models.ForeignKey(boardTempSensor, on_delete=models.CASCADE)
    data=models.FloatField(max_length=255)
    dataCreated = models.DateTimeField(default = datetime.now)
    def __str__(self):
        return "{}-{}".format(self.id, self.sensor)

class valveDevice(models.Model):
    farm = models.ForeignKey(farm, on_delete=models.CASCADE)
    valveNumber = models.CharField(max_length=10)
    valveType = models.CharField(max_length=1, choices=valveType, default='1')

    class Meta:
        ordering = ['farm', 'valveNumber']
    def __str__(self):
        return "{}-{}-{}".format(self.id, self.farm, self.valveNumber)

class relayDevice(models.Model):
    farm = models.ForeignKey(farm, on_delete=models.CASCADE)
    relayNumber = models.CharField(max_length=10)
    scheduleStatus=models.BooleanField(blank=True, null=True)
    currentStatus=models.BooleanField(blank=True, null=True)
    manualMode=models.BooleanField(blank=True, null=True, default=False)

    class Meta:
        ordering = ['farm', 'relayNumber']
    def __str__(self):
        return "{}-{}-{}".format(self.id, self.farm, self.relayNumber)


class valveData(models.Model):
    device = models.ForeignKey(valveDevice, on_delete=models.CASCADE)
    data=models.BooleanField(default=False)
    dataCreated = models.DateTimeField(default = datetime.now)
    def __str__(self):
        return "{}-{}".format(self.id, self.device)

class relayData(models.Model):
    device = models.ForeignKey(relayDevice, on_delete=models.CASCADE)
    data=models.BooleanField(default=False)
    dataCreated = models.DateTimeField(default = datetime.now)
    def __str__(self):
        return "{}-{}".format(self.id, self.device)


period_choice=[ ('0','0'),
                ('1','1'),
               ('2','2'),
               ('3','3'),
               ('4','4'),
               ('5','5'),
               ('6','6')]

class scheduleRelay(models.Model):
    relay=models.ForeignKey(relayDevice, on_delete=models.CASCADE, null=True)
    scheduleId=models.CharField(max_length=255, default="not assign")
    period=models.CharField(max_length=2, choices=period_choice, blank=True, default='0')
    startTime=models.CharField(max_length=10, blank=True, default="00:00")
    duration=models.IntegerField(default=0, blank=True)
    dayOfWeek=models.TextField(max_length=255, default="sun, mon, tue, wed, thu, fri, sat", blank=True)
    enable=models.BooleanField(default=False, blank=True)

    def __str__(self):
        return "{}".format(self.scheduleId)

    def updateScheduleName(self):
        self.scheduleId='{}_relay{}_period{}'.format(self.relay.farm.farmCode, self.relay.relayNumber, self.period)
        self.save()


