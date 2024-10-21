"""
URL configuration for proyectoDS project.

Th `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import home, homeCapataz, homeGerente, homeDirector, exit, group_users, prueba, dashboard, graficas, añadirObras, listarObras, borrarObra, actualizarObra, act_obra, informes

urlpatterns = [
    path('',home, name='home'), #Url vacia, esto significa que cuando se ingresa a la pagina principal sin ninguna extencion se abre el home
    path('homeCapataz/',homeCapataz, name='homeCapataz'), # Url para acceder al home de los capataz
    path('homeGerente/',homeGerente,name='homeGerente'),# Url para acceder al home del Gerente
    path('homeDirector/',homeDirector,name='homeDirector'),# Url para acceder al home del Director
    path ('logout/',exit, name='exit'), #URL que realiza el logout
    path('capataz/users/', group_users, name='group_users'), #URL en prueba para listar usuarios
    path ('prueba/',prueba, name='prueba'), #URL que realiza el logout
    path ('dashboard/',dashboard, name='dashboard'), #URL que nos manda al dashboard
    path ('graficas/',graficas, name='graficas'), #URL que nos manda a las graficas. 
    path('añadir_obras/', añadirObras, name='añadir_obras'),
    path('listar_obras/', listarObras, name='listar_obras'),
    path('listar_obras/borrar_obra/<int:id>/', borrarObra, name='borrar_obra'),
    path('listar_obras/actualizar_obra/<int:id>/', actualizarObra, name='actualizar_obra'),
    path('listar_obras/actualizar_obra/act_obra/<int:id>/', act_obra, name='act_obra'),
    path('subirInforme/',informes, name='subirInforme')
]
#HOLA 
#ADIOS