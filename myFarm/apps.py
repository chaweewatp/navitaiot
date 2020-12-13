from django.apps import AppConfig


class MyfarmConfig(AppConfig):
    name = 'myFarm'

    # def ready(self):
    #     """this function will be moved to view.py"""
    #     from myFarm import schedulejobs
    #     schedulejobs.start()

