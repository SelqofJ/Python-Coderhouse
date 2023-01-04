from django.db import models

# Create your models here.

class Curso (models.Model):
    nombre = models.CharField(max_length=64)
    comision = models.IntegerField()


class Estudiante (models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_de_nacimiento = models.DateField()
    bio = models.TextField()

"""

class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField()
    esta_aprobado = models.BooleanField(default=False)
"""
