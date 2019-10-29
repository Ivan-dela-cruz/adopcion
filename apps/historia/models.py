from django.db import models
from  django.contrib.auth.models import User
from apps.mascota.models import Mascota


class Historia(models.Model):
    id_historia =  models.AutoField(primary_key= True)
    id_mascota = models.ForeignKey(Mascota, on_delete = models.CASCADE)
    id_adoptivo = models.ForeignKey(User, on_delete = models.CASCADE)
    historias = models.TextField()
    fecha = models.DateField()
    like = models.IntegerField(blank=True)
    imagen = models.ImageField(blank=True)
    titulo = models.CharField(max_length=250)



