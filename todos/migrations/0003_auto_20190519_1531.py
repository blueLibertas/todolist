# Generated by Django 2.2.1 on 2019-05-19 15:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20190519_1452'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['priority', 'title']},
        ),
        migrations.AlterField(
            model_name='todo',
            name='duedate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 5, 26, 15, 31, 52, 479387), null=True),
        ),
    ]
