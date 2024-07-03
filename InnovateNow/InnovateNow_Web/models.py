from django.db import models

# Create your models here.


class Navbar(models.Model):
    id_navbar = models.AutoField(db_column="idNavbar", primary_key=True)
    nombre = models.CharField(max_length=50)
    url = models.CharField(max_length=100)

class QuienesSomos(models.Model):
    id_quienes_somos = models.AutoField(db_column="idQuienesSomos", primary_key=True)
    titulo = models.CharField(max_length=100)
    cuerpo = models.TextField()

class Servicio(models.Model):
    id_servicio = models.AutoField(db_column="idServicio", primary_key=True)
    nombre_servicio = models.CharField(max_length=50)
    tipo_servicio = models.CharField(max_length=50)
    descripcion = models.TextField()
    nombre_imagen = models.CharField(max_length=100)

class Testimonio(models.Model):
    id_testimonio = models.AutoField(db_column="idTestimonio", primary_key=True)
    nombre_persona = models.CharField(max_length=100)
    testimonio = models.TextField()
    imagen_testimonio = models.CharField(max_length=100, null=True)
