from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def registro_cancha(request):
    return render(request, 'registroCancha.html')

def reservar(request):
    return render(request, 'reservar.html')