from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    navbar = Navbar.objects.all()
    Testimonios = Testimonio.objects.all()
    context = {
        "Testimonios" : Testimonios,
        "Navbar": navbar,
    }
    return render(request, 'InnovateNow_Web/index.html', context)

def quienesSomos(request):
    navbar = Navbar.objects.all()
    quienesSomos = QuienesSomos.objects.all()
    context = {
        "Navbar": navbar,
        "QuienesSomos" : quienesSomos
    }
    return render(request, 'InnovateNow_Web/quienesSomos.html', context)

def servicios(request):
    navbar = Navbar.objects.all()
    servicios = Servicio.objects.all()
    context = {
        "Navbar": navbar,
        "Servicio" : servicios
    }
    return render(request, 'InnovateNow_Web/servicios.html', context)