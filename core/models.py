from django.db import models

class Obra(models.Model):
    idObra = models.IntegerField(null=True, blank=True)
    idDirector = models.IntegerField(null=True, blank=True)
    idCapataz = models.IntegerField(null=True, blank=True)
    idAyudante = models.IntegerField(null=True, blank=True)
    idPeon = models.IntegerField(null=True, blank=True)
    nombreObra = models.CharField(max_length=30)
    estadoObra = models.CharField(max_length=10)
    fechaInicioObra = models.DateField()

    class Meta:
        db_table='obra'




# Create your models here.
