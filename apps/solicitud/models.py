from django.db import models

from apps.mascota.models import Mascota
from  django.contrib.auth.models import User


class Solicitud(models.Model):
    id =  models.AutoField(primary_key= True)
    id_mascota = models.ForeignKey(Mascota, on_delete = models.CASCADE)
    id_user = models.ForeignKey(User, on_delete = models.CASCADE)
