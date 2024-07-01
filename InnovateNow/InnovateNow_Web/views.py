from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'InnovateNow_Web/index.html', context)

def quienesSomos(request):
    context = {}
    return render(request, 'InnovateNow_Web/quienesSomos.html', context)

def servicios(request):
    context = {}
    return render(request, 'InnovateNow_Web/servicios.html', context)