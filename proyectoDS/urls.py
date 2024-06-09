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
from django.contrib import admin
from django.urls import path, include

#Aqui se configuran los urls de administrador, y se importan las urls de la carpeta core, 
urlpatterns = [
    path('',include('core.urls')), #al usuario ingresar directamente va a las urls asignadas en la carpeta core
    path('admin/', admin.site.urls), #Por defecto de Django
    path('accounts/',include('django.contrib.auth.urls')), #Por defecto de Django
]
