from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def misionyvision(request):
    return render(request, 'misionyvision.html')

def porqueorion(request):
    return render(request, 'porqueorion.html')

def quebuscamos(request):
    return render(request, 'quebuscamos.html')

def login(request):
    return render(request, 'login.html')

def indexregistro(request):
    return render(request, 'registro-eleccion.html')

def registrociudadano(request):
    return render(request, 'registro-ciudadano.html')

def registroabogado(request):
    return render(request, 'registro-abogado.html')