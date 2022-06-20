from django.http import HttpResponse
from .models import Pizza
from django.shortcuts import render


def index(request):
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, 'pizzas/index.html', {'pizzas': pizzas})

