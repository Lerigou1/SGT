from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def index(request):
    return HttpResponse("Olá mundo, Que tistreza!")
    
def saudacao(request, nome):
    return render(request, 'index.html')

def ola(request, nome):
    return render(request, 'greet.html', {'name':nome})

def tiadozap(request, name):
    return render(request, 'tiadozap.html', {'name':name, 'dia':True})