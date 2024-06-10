from django.db import models

class Obra(models.Model):
    idObra = models.IntegerField()
    idUsuario = models.IntegerField()
    nombreObra = models.CharField(max_length=30)
    georeferencia =models.FileField()
    estadoObra = models.CharField(max_length=10)
    fechaInicioObra = models.DateField()
    archivos= models.FileField()

    class Meta:
        db_table='obra'
# Create your models here.
