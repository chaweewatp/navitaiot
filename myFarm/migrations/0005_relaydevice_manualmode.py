# Generated by Django 3.1.1 on 2020-12-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFarm', '0004_auto_20201213_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='relaydevice',
            name='manualMode',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
