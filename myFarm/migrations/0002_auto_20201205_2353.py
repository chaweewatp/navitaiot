# Generated by Django 3.1.1 on 2020-12-05 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFarm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedulerelay',
            name='dayOfWeek',
            field=models.TextField(blank=True, default='sun, mon, tue, wed, thu, fri, sat', max_length=255),
        ),
    ]
