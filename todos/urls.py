#from django.conf.urls import url
#from . import views
from .views import *
from django.urls import path

urlpatterns = [
    path('', TodoListView.as_view(), name = 'list'),
    path('add/', TodoCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', TodoDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', TodoUpdateView.as_view(), name='update'),
    path('complete/<int:pk>/', TodoUpdateCompleteView.as_view(), name='complete'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='delete'),
]
