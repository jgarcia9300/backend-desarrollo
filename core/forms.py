from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *
from .models import *

class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label='Group')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2','group']
        
class InformesForm(forms.ModelForm):
    class Meta:
        model = informes
        fields = ['idInforme','idUsuario','georeferencias','documento','notasDeVoz']
        
