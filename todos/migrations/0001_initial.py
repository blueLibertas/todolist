# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-19 09:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('duedate', models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 26, 9, 25, 18, 361560))),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-priority', 'title'],
            },
        ),
    ]
