from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.views.decorators.http import require_http_methods, require_POST
from .forms import *
from django.http import HttpResponse
from .models import *

# @login_required se utiliza para validar que el usuario esté logueado para poder acceder a la página respectiva.
@login_required
@require_http_methods(["GET"])
def home(request):
    if request.user.is_superuser:  # Si el usuario es un superuser, accederá al home destinado para el gerente.
        return redirect(dashboard)
    elif request.user.groups.filter(name='Director').exists():  # Si es un usuario perteneciente al grupo Director.
        return redirect(homeDirector)
    else:
        return redirect(homeCapataz)  # Si no cumple con ninguna de las anteriores, accederá al home del Capataz.

@login_required
@require_http_methods(["GET"])
def homeCapataz(request):
    obras = Obra.objects.all()
    if request.user.groups.filter(name='Capataz').exists():
        return render(request, 'frontend/Capataz/homeCapataz.html', {'obras': obras})
    return redirect('home')

@login_required
@require_http_methods(["GET", "POST"])
def homeGerente(request):
    if not request.user.is_superuser:
        return redirect('home')

    group_Ayudante = get_object_or_404(Group, name='Ayudante')
    users_Ayudante = group_Ayudante.user_set.all()
    group_Peon = get_object_or_404(Group, name='Peon')
    users_Peon = group_Peon.user_set.all()
    group_Director = get_object_or_404(Group, name='Director')
    users_Director = group_Director.user_set.all()
    group_Capataz = get_object_or_404(Group, name='Capataz')
    users_Capataz = group_Capataz.user_set.all()

    search_query_director = request.GET.get('search_director', '')
    search_query_capataz = request.GET.get('search_capataz', '')
    search_query_peon = request.GET.get('search_peon', '')
    search_query_ayudante = request.GET.get('search_ayudante', '')

    if search_query_director:
        users_Director = users_Director.filter(username__icontains=search_query_director)
    if search_query_capataz:
        users_Capataz = users_Capataz.filter(username__icontains=search_query_capataz)
    if search_query_peon:
        users_Peon = users_Peon.filter(username__icontains=search_query_peon)
    if search_query_ayudante:
        users_Ayudante = users_Ayudante.filter(username__icontains=search_query_ayudante)

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            group.user_set.add(user)
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
@require_http_methods(["GET", "POST"])
def homeDirector(request):
    if not request.user.groups.filter(name='Director').exists():
        return redirect('home')

    group_Director = get_object_or_404(Group, name='Director')
    users_Director = group_Director.user_set.all()
    group_Capataz = get_object_or_404(Group, name='Capataz')
    users_Capataz = group_Capataz.user_set.all()

    search_query = request.GET.get('search', '')
    if search_query:
        users_Capataz = users_Capataz.filter(username__icontains=search_query)
        users_Director = users_Director.filter(username__icontains=search_query)

    all_user = list(users_Capataz) + list(users_Director)

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return redirect('group_users')
        except User.DoesNotExist:
            pass

    return render(request, 'frontend/Director/homeDirector.html', {
        'group_capataz': group_Capataz,
        'users_capataz': users_Capataz,
        'group_gerente': group_Director,
        'users_gerente': users_Director,
        'all_user': all_user
    })

@login_required
@require_POST
def borrarObra(request, id):
    if request.user.is_superuser:
        borrarObra = get_object_or_404(Obra, idObra=id)
        borrarObra.delete()
    return redirect("listar_obras")

@login_required
@require_http_methods(["GET", "POST"])
def crearObra(request):
    if request.method == 'POST':
        form = CrearObraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_obras')
    else:
        form = CrearObraForm()

    return render(request, 'frontend/crearObra.html', {'form': form})

@login_required
@require_http_methods(["GET", "POST"])
def group_users(request):
    group_Director = get_object_or_404(Group, name='Director')
    users_Director = group_Director.user_set.all()
    group_Capataz = get_object_or_404(Group, name='Capataz')
    users_Capataz = group_Capataz.user_set.all()

    search_query = request.GET.get('search', '')
    if search_query:
        users_Capataz = users_Capataz.filter(username__icontains=search_query)
        users_Director = users_Director.filter(username__icontains=search_query)

    all_user = list(users_Capataz) + list(users_Director)

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return redirect('group_users')
        except User.DoesNotExist:
            pass

    return render(request, 'frontend/Gerente/group_users.html', {
        'group_capataz': group_Capataz,
        'users_capataz': users_Capataz,
        'group_gerente': group_Director,
        'users_gerente': users_Director,
        'all_user': all_user
    })

def prueba(request): 
    
        return render(request,'frontend/prueba.html')

@login_required
def dashboard(request):
    if request.user.is_superuser:
        return render(request, 'frontend/Gerente/dashboard.html')
    return redirect('home')

def graficas(request): 
    
        return render(request,'frontend/Gerente/graficas.html')

@login_required
@require_http_methods(["POST"])
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

@login_required
def listarObras(request):
    obras = Obra.objects.all()
    return render(request, "frontend/listarObras.html", {'obras': obras})

@login_required
@require_http_methods(["GET", "POST"])
def actualizarObra(request, id):
    actualizarObra = get_object_or_404(Obra, idObra=id)
    if request.method == 'POST':
        nombreObra = request.POST.get('nombreObra')
        estadoObra = request.POST.get('estadoObra')
        fechaInicioObra = request.POST.get('fechaInicioObra')

        actualizarObra.nombreObra = nombreObra
        actualizarObra.estadoObra = estadoObra
        actualizarObra.fechaInicioObra = fechaInicioObra
        actualizarObra.save()
        return redirect("listar_obras")

    return render(request, "frontend/actualizarObra.html", {'actualizarObra': actualizarObra})

@require_http_methods(["POST"])
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

@require_http_methods(["POST"])
def informes(request):
    obras = Obra.objects.all()
    formInformes = InformesForm()  # Inicializar el formulario fuera del bloque 'if'
    if request.method == 'POST':
        formInformes = InformesForm(request.POST)
        if formInformes.is_valid():
            formInformes.save()  # Guardar el nuevo informe
            return redirect('asignarTareas')
    
    return render(request, "frontend/subirInforme.html", {'formInformes': formInformes, 'obras': obras})

def exit(request):
    logout(request)
    return redirect('home')