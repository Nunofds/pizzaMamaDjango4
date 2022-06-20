from django.urls import path
from . import views

app_name = 'pattes'

urlpatterns = [
    path('',  views.index, name='index')
]
