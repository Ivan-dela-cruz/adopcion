from django.db import models

class Propietario (models.Model):
    id =  models.AutoField(primary_key= True)
    ci_pro = models.CharField(max_length=11)
    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    edad = models.IntegerField()


    def __str__(self):
        return self.nombre
