from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('quienesSomos', views.quienesSomos, name="quienesSomos"),
    path('servicios', views.servicios, name="servicios"),
]