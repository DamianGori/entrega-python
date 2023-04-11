from django.shortcuts import render, redirect
from django import forms
from login.forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.contrib.auth.models import User
from login.forms import UserEditForm, UserEditPassword

# Create your views here.

def login_request(request):
      
      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
                  user = authenticate(username = usuario , password = contra)
                 
                  if user is not None:
                        login(request, user)
                        return render (request, "index.html", {"mensaje": f"Bienvenido/a {usuario}"})

                  else:
                        return render (request, "index.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "index.html", {"mensaje":"Formulario erroneo"})
      
      form = AuthenticationForm()
    
      return render(request, "login.html", {'form': form})


def logout_request(request):
      logout(request)
      mensaje_logout = {"mensaje_logout":"Saliste sin problemas"}
     # mensaje.info(request, "Saliste sin problemas")
      return render(request, "logout.html")


def register(request):
      if request.method == "POST":

            form = UserRegisterForm(request.POST)
            
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request, "index.html", {"mensaje": "usuario creado"})

      form = UserRegisterForm(request.POST)      
      return render(request, "registro.html", {"form": form})


@login_required
def EditarPerfil(request):
      usuario = request.user

      if request.method == "POST":
            miformulario = UserEditForm(request.POST)

            if miformulario.is_valid():
                  informacion = miformulario.cleaned_data

                  usuario.username = informacion["username"]
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  miformulario.save()

                  return render(request, "index.html", {"mensaje_edicion":"El usuario se editó correctamente"})

      else:
            miformulario = UserEditForm(initial={"usuario":usuario.username})


      return render(request, "editar_usuario.html", {"miformulario":miformulario, "usuario":usuario})

