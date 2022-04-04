from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

item_actual=""

def index(request):
    return render(request, 'interfaz_estado.html')
