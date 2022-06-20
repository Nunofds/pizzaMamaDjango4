from django.shortcuts import render
from .models import Pattes


def index(request):
    pattes = Pattes.objects.all().order_by('prix')
    return render(request, 'pattes/index.html', {'pattes': pattes})
