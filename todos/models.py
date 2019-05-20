# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
from datetime import datetime, timedelta, date

class Todo(models.Model):
    priority = models.PositiveIntegerField(blank=True, null=True)
    title = models.CharField(max_length = 250)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank = True)
    duedate = models.DateField(default = (datetime.now()+timedelta(days=7)), blank=True, null=True)
    completed = models.BooleanField(default = False)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed', 'priority', 'title']

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def past_duedate(self):
        return date.today() > self.duedate

    def dateString(self):
        return str(self.duedate)
