from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import Group


#@login required se utiliza para validar que el usuario este logueado para poder acceder a la pagina respectiva
@login_required
def home(request):
    if request.user.is_superuser: #Si es usuario es un superuser accedera al home destinado para el gerente
        return redirect(homeGerente)
    if request.user.groups.filter(name='Director').exists(): #Si es un usuario perteneciente al grupo Director accedera al home destinado para el Director
        return redirect(homeDirector)
    else:
        return redirect(homeCapataz) #si el usuario no cumple con ninguna de las anteriores accedera al home capataz diseñado para los capataces y los ayudantes
        
@login_required
def homeCapataz(request): #Pagina de inicio de los Capataz
    if request.user.groups.filter(name='Capataz').exists():#Se realiza otra validacion al momento de ingresar a la pagina
        return render(request,'core/homeCapataz.html')

@login_required
def homeGerente(request): #Pagina de inicio del gerente
    if request.user.is_superuser: #Se realiza otra validacion al momento de ingresar a la pagina
        return render(request,'core/homeGerente.html')

@login_required
def homeDirector(request): #Pagina de inicio del director
    if request.user.groups.filter(name='Director').exists():#Se realiza otra validacion al momento de ingresar a la pagina
     return render(request,'core/homeDirector.html')
    
def exit(request): # el exit define que el usuario cerro sesión y redirige al home donde al no estar logueado se va directamente al login
    logout(request)
    return redirect('home')

def group_users(request): #Esta es una prueba para listar usuarios pertenecientes a un grupo, aun no esta lista
    group = get_object_or_404(Group, name='Capataz')
    users = group.user_set.all()
    return render(request, 'core/group_users.html', {'group': group, 'users': users})



