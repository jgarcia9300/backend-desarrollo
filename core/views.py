from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from .forms import *


#@login required se utiliza para validar que el usuario este logueado para poder acceder a la pagina respectiva
@login_required
def home(request):
    if request.user.is_superuser: #Si es usuario es un superuser accedera al home destinado para el gerente
        return redirect(dashboard)
    if request.user.groups.filter(name='Director').exists(): #Si es un usuario perteneciente al grupo Director accedera al home destinado para el Director
        return redirect(homeDirector)
    else:
        return redirect(homeCapataz) #si el usuario no cumple con ninguna de las anteriores accedera al home capataz diseñado para los capataces y los ayudantes
        
@login_required
def homeCapataz(request): #Pagina de inicio de los Capataz
    if request.user.groups.filter(name='Capataz').exists():#Se realiza otra validacion al momento de ingresar a la pagina
        return render(request,'frontend/homeCapataz.html')

@login_required
def homeGerente(request): #Pagina de inicio del gerente

    group_Director = get_object_or_404(Group, name='Director')
    users_Director = group_Director.user_set.all()

    group_Capataz = get_object_or_404(Group, name='Capataz')
    users_Capataz = group_Capataz.user_set.all()

    if request.user.is_superuser: #Si el usuario que realiza el logueo es superuser entonces entra al homeGerente
        if request.method == 'POST': #se define que si el metodo es igual a POST se realizara 
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save() #guarda los datos
                group = form.cleaned_data['group'] 
                group.user_set.add(user) #Se añade el usuario al grupo
                return redirect('homeGerente')
        else:
            form = CustomUserCreationForm()
        return render(request, 'frontend/Gerente/homeGerente.html', {
            'group_capataz': group_Capataz,
            'users_capataz': users_Capataz,
            'group_gerente': group_Director,
            'users_gerente': users_Director,
            'form': form
        })

@login_required
def homeDirector(request): #Pagina de inicio del director
    if request.user.groups.filter(name='Director').exists():#Se realiza otra validacion al momento de ingresar a la pagina
     return render(request,'frontend/homeDirector.html')
    
def exit(request): # el exit define que el usuario cerro sesión y redirige al home donde al no estar logueado se va directamente al login
    logout(request)
    return redirect('home')


@login_required
def group_users(request): #Esta es una prueba para listar usuarios pertenecientes a un grupo, aun no esta lista
    group = get_object_or_404(Group, name='Capataz')
    users = group.user_set.all()
    search_query = request.GET.get('search', '')

    if search_query:
        users = users.filter(username__icontains=search_query)

    elif request.method == 'POST':
        user_id = request.POST.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            # Redirige a donde quieras después de eliminar el usuario
            return redirect('group_users')
        except User.DoesNotExist:
            # Manejar el caso donde el usuario no existe
            pass
    return render(request, 'frontend/Gerente/group_users.html', {'group': group, 'users': users})


def prueba(request): 
    
        return render(request,'frontend/prueba.html')

def dashboard(request): 
    
        return render(request,'frontend/Gerente/dashboard.html')

def graficas(request): 
    
        return render(request,'frontend/Gerente/graficas.html')



