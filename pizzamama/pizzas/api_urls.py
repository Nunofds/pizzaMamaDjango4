from . import views
from django.urls import path

app_name = 'pizzas'

urlpatterns = [
    path('GetPizzas/', views.api_get_pizzas),
]
