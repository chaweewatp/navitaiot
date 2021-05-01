from django.apps import AppConfig
from .__init__ import scheduler
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution


class MyiotConfig(AppConfig):
    name = 'myiot'

    def ready(self):
        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.start()
