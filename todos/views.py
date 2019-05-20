# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Todo
from datetime import date

# Create your views here.
class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields =  ['priority', 'title', 'text', 'duedate']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class TodoDetailView(DetailView):
    model = Todo

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['priority', 'title', 'text', 'duedate']
    success_url = reverse_lazy('list')
    template_name_suffix = '_update'

class TodoUpdateCompleteView(UpdateView):
    model = Todo
    fields = ['completed']
    success_url = reverse_lazy('list')
    template_name_suffix = '_complete'

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('list')
