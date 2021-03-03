# Generated by Django 3.1.1 on 2020-12-13 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myFarm', '0003_auto_20201206_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='relaydevice',
            name='currentStatus',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='relaydevice',
            name='scheduleStatus',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedulerelay',
            name='relay',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myFarm.relaydevice'),
        ),
    ]