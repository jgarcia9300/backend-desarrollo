from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from .forms import *
from django.http import HttpResponse
from .models import *





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
        return render(request,'frontend/Capataz/homeCapataz.html')

@login_required
def homeGerente(request):
    if request.user.is_superuser:
    # Obtener los grupos y sus usuarios
        group_Ayudante = get_object_or_404(Group, name='Ayudante')
        users_Ayudante = group_Ayudante.user_set.all()

        group_Peon = get_object_or_404(Group, name='Peon')
        users_Peon = group_Peon.user_set.all()

        group_Director = get_object_or_404(Group, name='Director')
        users_Director = group_Director.user_set.all()

        group_Capataz = get_object_or_404(Group, name='Capataz')
        users_Capataz = group_Capataz.user_set.all()

        # Obtener los términos de búsqueda
        search_query_director = request.GET.get('search_director', '')
        search_query_capataz = request.GET.get('search_capataz', '')
        search_query_peon = request.GET.get('search_capataz', '')
        search_query_ayudante = request.GET.get('search_capataz', '')

        # Filtrar los usuarios según los términos de búsqueda
        if search_query_director:
            users_Director = users_Director.filter(username__icontains=search_query_director)
        
        if search_query_capataz:
            users_Capataz = users_Capataz.filter(username__icontains=search_query_capataz)
        if search_query_peon:
            users_Director = users_Peon.filter(username__icontains=search_query_director)
        if search_query_ayudante:
            users_Director = users_Ayudante.filter(username__icontains=search_query_peon)

        if request.user.is_superuser:  # Verificar si el usuario es superuser
            if request.method == 'POST':
                form = CustomUserCreationForm(request.POST)
                if form.is_valid():
                    user = form.save()  # Guardar el nuevo usuario
                    group = form.cleaned_data['group']
                    group.user_set.add(user)  # Añadir el usuario al grupo
                    return redirect('homeGerente')
            else:
                form = CustomUserCreationForm()

            return render(request, 'frontend/Gerente/homeGerente.html', {
                'group_capataz': group_Capataz,
                'users_capataz': users_Capataz,
                'group_director': group_Director,
                'users_director': users_Director,
                'group_ayudante': group_Ayudante,
                'users_ayudante': users_Ayudante,
                'group_peon': group_Peon,
                'users_peon': users_Peon,
                'form': form
            })

@login_required
def homeDirector(request): #Pagina de inicio del director
    if request.user.groups.filter(name='Director').exists():#Se realiza otra validacion al momento de ingresar a la pagina
        group_Director = get_object_or_404(Group, name='Director')
        users_Director = group_Director.user_set.all()
        search_query = request.GET.get('search', '')

        group_Capataz = get_object_or_404(Group, name='Capataz')
        users_Capataz = group_Capataz.user_set.all()
        search_query = request.GET.get('search', '')

        
        search_query = request.GET.get('search', '')

        if search_query:
            users_Capataz = users_Capataz.filter(username__icontains=search_query)
            users_Director = users_Director.filter(username__icontains=search_query)

        all_user = list(users_Capataz)+list(users_Director)
        if request.method == 'POST':
            user_id = request.POST.get('user_id')
            try:
                user = User.objects.get(id=user_id)
                user.delete()
                # Redirige a donde quieras después de eliminar el usuario
                return redirect('group_users')
            except User.DoesNotExist:
                # Manejar el caso donde el usuario no existe
                pass
        return render(request, 'frontend/Director/homeDirector.html',
                {
                'group_capataz': group_Capataz,
                'users_capataz': users_Capataz,
                'group_gerente': group_Director,
                'users_gerente': users_Director,
                'all_user': all_user})
    
def exit(request): # el exit define que el usuario cerro sesión y redirige al home donde al no estar logueado se va directamente al login
    logout(request)
    return redirect('home')


@login_required
def group_users(request): #Esta es una prueba para listar usuarios pertenecientes a un grupo, aun no esta lista
    group_Director = get_object_or_404(Group, name='Director')
    users_Director = group_Director.user_set.all()
    search_query = request.GET.get('search', '')

    group_Capataz = get_object_or_404(Group, name='Capataz')
    users_Capataz = group_Capataz.user_set.all()
    search_query = request.GET.get('search', '')

    
    search_query = request.GET.get('search', '')

    if search_query:
        users_Capataz = users_Capataz.filter(username__icontains=search_query)
        users_Director = users_Director.filter(username__icontains=search_query)

    all_user = list(users_Capataz)+list(users_Director)
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            # Redirige a donde quieras después de eliminar el usuario
            return redirect('group_users')
        except User.DoesNotExist:
            # Manejar el caso donde el usuario no existe
            pass
    return render(request, 'frontend/Gerente/group_users.html', {
            'group_capataz': group_Capataz,
            'users_capataz': users_Capataz,
            'group_gerente': group_Director,
            'users_gerente': users_Director,
            'all_user': all_user
            })

@login_required
def añadirObras(request): 

    group_Ayudante = get_object_or_404(Group, name='Ayudante')
    users_Ayudante = group_Ayudante.user_set.all()

    group_Peon = get_object_or_404(Group, name='Peon')
    users_Peon = group_Peon.user_set.all()

    group_Director = get_object_or_404(Group, name='Director')
    users_Director = group_Director.user_set.all()

    group_Capataz = get_object_or_404(Group, name='Capataz')
    users_Capataz = group_Capataz.user_set.all()


    if request.method == 'POST':
        idObra = request.POST.get('idObra')
        idDirector = request.POST.get('idDirector')
        idCapataz = request.POST.get('idCapataz')
        idAyudante = request.POST.get('idAyudante')
        idPeon = request.POST.get('idPeon')
        nombreObra = request.POST.get('nombreObra')
        estadoObra = request.POST.get('estadoObra')
        fechaInicioObra = request.POST.get('fechaInicioObra')

        # Crear instancia del modelo Obra y guardar en la base de datos
        obra = Obra(
            idObra=idObra,
            idDirector = idDirector,
            idCapataz = idCapataz,
            idAyudante = idAyudante,
            idPeon = idPeon,
            nombreObra=nombreObra,
            estadoObra=estadoObra,
            fechaInicioObra=fechaInicioObra,
        )
        obra.save()
        return HttpResponse('Obra añadida con exito')
    else:
        return render(request,'frontend/añadirObras.html',{
                            'group_capataz': group_Capataz,
                'users_capataz': users_Capataz,
                'group_director': group_Director,
                'users_director': users_Director,
                'group_ayudante': group_Ayudante,
                'users_ayudante': users_Ayudante,
                'group_peon': group_Peon,
                'users_peon': users_Peon,
        })


def prueba(request): 
    
        return render(request,'frontend/prueba.html')

def dashboard(request): 
    if request.user.is_superuser:
        return render(request,'frontend/Gerente/dashboard.html')
    elif request.user.groups.filter(name='Director').exist():
        return render(request,'frontend/Director/homeDirector.html')

def graficas(request): 
    
        return render(request,'frontend/Gerente/graficas.html')

@login_required
def listarObras(request):
        
        group_Ayudante = get_object_or_404(Group, name='Ayudante')
        users_Ayudante = group_Ayudante.user_set.all()

        group_Peon = get_object_or_404(Group, name='Peon')
        users_Peon = group_Peon.user_set.all()

        group_Director = get_object_or_404(Group, name='Director')
        users_Director = group_Director.user_set.all()

        group_Capataz = get_object_or_404(Group, name='Capataz')
        users_Capataz = group_Capataz.user_set.all()

        obras = Obra.objects.all()
        return render(request, 'frontend/listarObras.html', {'obras': obras, 
                'group_capataz': group_Capataz,
                'users_capataz': users_Capataz,
                'group_director': group_Director,
                'users_director': users_Director,
                'group_ayudante': group_Ayudante,
                'users_ayudante': users_Ayudante,
                'group_peon': group_Peon,
                'users_peon': users_Peon,})

def borrarObra(request,id):
  borrarObra = Obra.objects.get(idObra=id)
  borrarObra.delete()
  return redirect("listar_obras")

def actualizarObra(request,id):
    actualizarObra = Obra.objects.get(idObra=id)
    return render(request, "frontend/actualizarObra.html", {'actualizarObra':actualizarObra})

def act_obra(request,id):
        nombreObra = request.POST.get('nombreObra')
        estadoObra = request.POST.get('estadoObra')
        fechaInicioObra = request.POST.get('fechaInicioObra')
        actualizarObra = Obra.objects.get(idObra=id)
        actualizarObra.nombreObra = nombreObra
        actualizarObra.estadoObra = estadoObra
        actualizarObra.fechaInicioObra = fechaInicioObra
        actualizarObra.save()
        return redirect("listar_obras")


def informes (request):
    if request.method == 'POST':
        formInformes = InformesForm(request.POST)
        if formInformes.is_valid():
            formInformes.save()  # Guardar el nuevo usuario
            return redirect('asignarTareas')
        else:
            formInformes = InformesForm()
    return render(request,"frontend/asignarTareas",{'formInformes' : formInformes})


