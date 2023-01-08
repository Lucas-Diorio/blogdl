from django.shortcuts import render

from .models import *
from django.http import HttpResponse
from usuarios.forms import *
from blog.views import *

#Para formulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import  PasswordChangeForm

# para restriciones
from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clases
from django.contrib.auth.decorators import login_required #para vistas basadas en objetos

# CRUD
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Avatar
def obtenerAvatar(request):
    if request.user.is_authenticated:
        lista = Perfil.objects.filter(user=request.user)
        if len(lista)!=0:
            imagen = lista[0].avatar.url
        else:
            imagen = ""
    else:
        imagen = ""
    return imagen

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
                return render(request, 'usuarios/user.html')
            else: 
                return render(request, 'usuarios/login.html', {'mensaje': 'Usuario o contraseña incorrectos', "form": AuthenticationForm})
        else:
            return render(request, 'usuarios/login.html', {'mensaje':"Usuario o contraseña incorrectos", "form": AuthenticationForm}) 


    else:
        form = AuthenticationForm()
    return render(request, "usuarios/login.html", {"form": form, "mensaje": "Bienvenido nuevamente"})

# register
def Register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            return render(request, 'usuarios/user.html', {'mensaje':"Usuario creado correctamente"})
        else:
            return render(request, "usuarios/register.html", {"form":form}, {"mensaje": "Hubo un error, intente nuevamente."})
    else:
        form = RegisterForm()
    return render(request, "usuarios/register.html", {"form":form, "mensaje": "Registrar usuario"})

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
            return render(request, "usuarios/editUser.html", {"form":form, "nombreusuario":usuario.first_name, "mensaje": "Error al editar el perfil, intente nuevamente"})  
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "usuarios/editUser.html", {"form":form, "nombreusuario":usuario.first_name})

@ login_required
def perfil_edit(request):
    datos_viejos = Perfil.objects.filter(user = request.user)
    if datos_viejos:
        formulario_edit = Form_Perfil(initial={"descripcion": datos_viejos[0].descripcion, "avatar": datos_viejos[0].avatar})
    else:
        formulario_edit = Form_Perfil()
    if request.method == "POST":
        formulario = Form_Perfil(request.POST, request.FILES)
        if formulario.is_valid():
            datos_viejos = Perfil.objects.filter(user = request.user)
            if datos_viejos != None:        # Si existe, lo elimina primero para evitar multiples entradas.
                datos_viejos.delete()
            datos_nuevos = Perfil(user=request.user, descripcion = request.POST["descripcion"], avatar = request.FILES["avatar"] )
            datos_nuevos.save()
            return render(request, "usuarios/user.html", {"mensaje": "El perfil ha sido editado exitosamente!"})
        else:
            return render(request, "usuarios/perfil_edit.html", {"form_edit_perfil" : formulario_edit, "mensaje": "Intentelo Nuevamente, hubo un error"})
    else:
        return render(request, "usuarios/perfil_edit.html", {"form_edit_perfil": formulario_edit, "mensaje": "Editar perfil"})


@ login_required
def user_perfil(request):
    data_perfil = Perfil.objects.filter(user = request.user)
    if data_perfil:
        descripcion = data_perfil[0].descripcion
        
    else:
        descripcion = ""
        
    return render(request, "usuarios/userperfil.html", {"user" : request.user, "avatar": obtenerAvatar(request)})


@ login_required
def user_logout(request):
    logout(request)
    return render(request, "usuarios/logout.html", {"mensaje": "Has cerrado sesion!"})