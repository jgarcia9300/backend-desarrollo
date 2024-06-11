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

class informes(models.Model):
    idInforme = models.IntegerField(null=True, blank=True)
    idUsuario = models.IntegerField(null=True, blank=True)
    georeferencias = models.FileField(upload_to='media/', null=True, blank=True)
    documento = models.FileField(upload_to='media/', null=True, blank=True)
    notasDeVoz = models.FileField(upload_to='media/', null=True, blank=True)

    class Meta:
        db_table='informes'

class Avances(models.Model):
    idUsuario = models.IntegerField(null=True, blank=True)
    porcentajeAvance= models.IntegerField(null=True, blank=True)

    class Meta:
        db_table='Avances'

class asignarTareas(models.Model):
    idDirector = models.IntegerField(null=True,blank=True)
    idCapataz = models.IntegerField(null=True, blank=True)
    idAyudante = models.IntegerField(null=True, blank=True)
    idPeon = models.IntegerField(null=True, blank=True)
    descripcion = models.TextField()

    class Meta:
        db_table='asignarTareas'


# Create your models here.
