from django.db import models


# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    genero = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
