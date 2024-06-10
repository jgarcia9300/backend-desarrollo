from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label='Group')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2','group']
        
