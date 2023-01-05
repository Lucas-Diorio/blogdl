from django.shortcuts import render

from .models import *
from django.http import HttpResponse
from usuarios.forms import *

#Para formulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# para restriciones
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clases
from django.contrib.auth.decorators import login_required #para vistas basadas en objetos

# CRUD
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
def userPage(request):
    return render(request, "usuarios/user.html")



# login

def Login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")

            usuario=authenticate(username=usu, password=clave)#trae un usuario de la base con ese usuario y pass
            if usuario is not None:
                login(request, usuario)
                return render(request, 'blog/inicio.html', {'mensaje': f'Bienvenido{usuario}'})
            else: 
                return render(request, 'blog/inicio.html', {'mensaje': 'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'usuarios/login.html', {'mensaje':"Usuario o contraseña incorrectos", "form": form}) 


    else:
        form = AuthenticationForm()
    return render(request, "usuarios/login.html", {"form": form})

# register
def Register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request, 'usuarios/index.html', {'mensaje':"usuario creado correctamente"})
    else:
        form = RegisterForm()
    return render(request, "usuarios/register.html", {"form":form})

# edituser
@login_required
def editUser(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "usuarios/user.html", {"mensaje":"Perfil editado correctamente"})
        else:
            return render(request, "usuarios/editUser.html", {"form":form, "nombreusuario":usuario.first_name, "mensaje": "Error al editar el perfil"})  
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "usuarios/editUser.html", {"form":form, "nombreusuario":usuario.first_name})
