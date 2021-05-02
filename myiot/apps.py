from django.apps import AppConfig
from .__init__ import scheduler, client



class MyiotConfig(AppConfig):
    name = 'myiot'

    def ready(self):
        from django_apscheduler.jobstores import DjangoJobStore
        from django_apscheduler.models import DjangoJobExecution
        scheduler.add_jobstore(DjangoJobStore(), "default")
        print('sheduler jobstore added')
        scheduler.start()
        print('sheduler start')



