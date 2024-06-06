from django.shortcuts import render


def index(request):
    return render(request, 'places/index.html')

def add(request):
    return render(request, 'places/add.html')