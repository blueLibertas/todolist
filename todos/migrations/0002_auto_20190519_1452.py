# Generated by Django 2.2.1 on 2019-05-19 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='duedate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 5, 26, 14, 52, 39, 829000), null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
