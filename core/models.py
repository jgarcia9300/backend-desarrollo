from django.db import models

class Obra(models.Model):
    idObra = models.FloatField()
    idUsuario = models.IntegerField()
    nombreObra = models.TextField()
    georeferencia =models.ImageField()
    estadoObra = models.TextField()
    fechaInicioObra = models.DateTimeField()
    archivos= models.FileField()
# Create your models here.
