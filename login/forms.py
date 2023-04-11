from django import forms
from dataclasses import fields
from django import forms 
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from . import models

class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repita la contraseña', widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', "email", "first_name", "last_name"]
        help_texts= {k:"" for k in fields}


class UserEditForm(forms.Form):
    username = forms.CharField(label="Nuevo nombre de usuario", required=None)
    password1 = forms.CharField(label= 'Nueva contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repita la contraseña', widget=forms.PasswordInput)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)

class UserEditPassword(PasswordChangeForm):
    password1 = forms.CharField(label= 'Nueva contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repita la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['password1', 'password2']
        help_texts= {k:"" for k in fields}