# Generated by Django 3.1.1 on 2020-12-06 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFarm', '0002_auto_20201205_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulerelay',
            name='period',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='0', max_length=2),
        ),
        migrations.AddField(
            model_name='schedulerelay',
            name='startTime',
            field=models.CharField(blank=True, default='00:00', max_length=10),
        ),
    ]
