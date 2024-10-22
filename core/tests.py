from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from core.models import Obra, informes, Avances, asignarTareas
from datetime import date

class ObraModelTest(TestCase):
    def test_create_obra(self):
        # Crear una instancia de Obra y verificar los campos
        obra = Obra.objects.create(
            idObra=1,
            idDirector=101,
            idCapataz=201,
            idAyudante=301,
            idPeon=401,
            nombreObra="Construcción A",
            estadoObra="Activa",
            fechaInicioObra=date(2024, 1, 1)
        )
        self.assertEqual(obra.idObra, 1)
        self.assertEqual(obra.idDirector, 101)
        self.assertEqual(obra.nombreObra, "Construcción A")
        self.assertEqual(obra.estadoObra, "Activa")
        self.assertEqual(obra.fechaInicioObra, date(2024, 1, 1))

class InformesModelTest(TestCase):
    def test_create_informe(self):
        # Simular la carga de archivos
        geo_file = SimpleUploadedFile("geo.txt", b"Georeferencia data")
        doc_file = SimpleUploadedFile("doc.txt", b"Documento data")
        audio_file = SimpleUploadedFile("audio.mp3", b"Audio data")
        
        informe = informes.objects.create(
            idInforme=1,
            idUsuario=101,
            georeferencias=geo_file,
            documento=doc_file,
            notasDeVoz=audio_file
        )
        self.assertEqual(informe.idInforme, 1)
        self.assertEqual(informe.idUsuario, 101)

        self.assertTrue(informe.documento.name.startswith("media/doc"))
        self.assertTrue(informe.documento.name.endswith(".txt"))

        self.assertTrue(informe.georeferencias.name.startswith("media/geo"))
        self.assertTrue(informe.georeferencias.name.endswith(".txt"))

        self.assertTrue(informe.notasDeVoz.name.startswith("media/audio"))
        self.assertTrue(informe.notasDeVoz.name.endswith(".mp3"))

    def test_delete_informe(self):
        # Crear y luego eliminar una instancia de informes
        informe = informes.objects.create(
            idInforme=1,
            idUsuario=101
        )
        informe_id = informe.id
        informe.delete()

        # Verificar que la instancia haya sido eliminada
        self.assertFalse(informes.objects.filter(id=informe_id).exists())

class AvancesModelTest(TestCase):
    def test_create_avance(self):
        # Crear una instancia de Avances y verificar los campos
        avance = Avances.objects.create(
            idUsuario=101,
            porcentajeAvance=75
        )
        self.assertEqual(avance.idUsuario, 101)
        self.assertEqual(avance.porcentajeAvance, 75)

    def test_update_avance(self):
        # Crear y luego actualizar una instancia de Avances
        avance = Avances.objects.create(
            idUsuario=101,
            porcentajeAvance=75
        )
        avance.porcentajeAvance = 85
        avance.save()

        # Verificar que los cambios se hayan guardado
        self.assertEqual(avance.porcentajeAvance, 85)
    


class AsignarTareasModelTest(TestCase):
    def test_create_asignar_tareas(self):
        # Crear una instancia de asignarTareas y verificar los campos
        tarea = asignarTareas.objects.create(
            idDirector=101,
            idCapataz=201,
            idAyudante=301,
            idPeon=401,
            descripcion="Tarea de prueba"
        )
        self.assertEqual(tarea.idDirector, 101)
        self.assertEqual(tarea.descripcion, "Tarea de prueba")

    def test_update_asignar_tareas(self):
        # Crear y luego actualizar una instancia de asignarTareas
        tarea = asignarTareas.objects.create(
            idDirector=101,
            descripcion="Tarea inicial"
        )
        tarea.descripcion = "Tarea modificada"
        tarea.save()

        # Verificar que los cambios se hayan guardado
        self.assertEqual(tarea.descripcion, "Tarea modificada")

    def test_delete_asignar_tareas(self):
        # Crear y luego eliminar una instancia de asignarTareas
        tarea = asignarTareas.objects.create(
            idDirector=101,
            descripcion="Tarea de prueba"
        )
        tarea_id = tarea.id
        tarea.delete()
        
# Verificar que la instancia haya sido eliminada
        self.assertFalse(asignarTareas.objects.filter(id=tarea_id).exists())

#Verificando actualizacion
    def test_update_informe(self):
        # Crear y luego actualizar una instancia de informes
        informe = informes.objects.create(
            idInforme=1,
            idUsuario=101
        )
        informe.idUsuario = 202
        informe.save()

        # Verificar que los cambios se hayan guardado
        self.assertEqual(informe.idUsuario, 202)
        
        