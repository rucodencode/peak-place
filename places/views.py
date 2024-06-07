from django.shortcuts import render
from .models import Place


def index(request):
    places = Place.objects.all()
    context = {
        'places': places
    }

    return render(request, 'places/index.html', context)

def add(request):
    return render(request, 'places/add.html')