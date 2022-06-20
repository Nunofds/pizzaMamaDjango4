# créer les chemins des views
from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name='index'),
]
