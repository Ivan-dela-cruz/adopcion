from django.db import models

class Mascota(models.Model):
    #datos principales
    id_mascota = models.AutoField(primary_key=True)
    ci_pro = models.CharField(max_length=250)
    nombre = models.CharField(max_length=250,blank=True)
    raza = models.CharField(max_length=250,blank=True)
    edad = models.IntegerField()
    descripcion = models.TextField(blank=True)

    #descipcion fisica
    tamanio = models.CharField(max_length=250)
    sexo = models.CharField(max_length=50)

    #salud
    alergia = models.CharField(max_length=10,blank=True)
    tratamiento = models.CharField(max_length=10,blank=True)
    enfermeda = models.CharField(max_length=10,blank=True)
    vacuna = models.CharField(max_length=10,blank=True)

    #sociabilidad
    adultos = models.CharField(max_length=10,blank=True)
    ninios = models.CharField(max_length=10,blank=True)
    otros = models.CharField(max_length=10,blank=True)

    #comportamiento
    carinioso = models.IntegerField()
    jugueton = models.IntegerField()
    tranquilo = models.IntegerField()
    educado = models.IntegerField()

    #hitoria
    mihistoria = models.TextField()

    #estatus
    estado = models.CharField(max_length=20)

    #fotos
    foto = models.ImageField( blank=True)



