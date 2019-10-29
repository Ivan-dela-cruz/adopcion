from django.db import models

class Adoptivo(models.Model):
    id_adoptivo = models.AutoField(primary_key= True)
    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    ci_adop = models.CharField(max_length=11)
    direccion = models.CharField(max_length=250)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    edad = models.IntegerField()

