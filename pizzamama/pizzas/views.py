from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from .models import Pizza


def index(request):
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, 'pizzas/index.html', {'pizzas': pizzas})


def api_get_pizzas(request):
    pizzas = Pizza.objects.all().order_by('prix')
    json = serializers.serialize('json', pizzas)
    return HttpResponse(json)

