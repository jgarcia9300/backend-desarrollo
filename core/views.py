from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def home(request):
    if request.user.is_superuser:
        return redirect(homeGerente)
    if request.user.groups.filter(name='Director').exists():
        return redirect(homeDirector)
    else:
        return redirect(homeCapataz)
        
@login_required
def homeCapataz(request):
    if request.user.groups.filter(name='Capataz').exists():
        return render(request,'core/homeCapataz.html')

@login_required
def homeGerente(request):
    if request.user.is_superuser:
        return render(request,'core/homeGerente.html')

@login_required
def homeDirector(request):
    if request.user.groups.filter(name='Director').exists():
     return render(request,'core/homeDirector.html')
    
def exit(request):
    logout(request)
    return redirect('home')






