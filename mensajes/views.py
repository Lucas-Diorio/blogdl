from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .models import *
from django.http import HttpResponse
from mensajes.forms import *

from django.utils.functional import SimpleLazyObject

# Create your views here.
def portada(request):
    return render(request, "mensajes/portada.html")

def mensajeFormulario(request):
    usuario=request.user 
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        
        if form.is_valid():
            informacion = form.cleaned_data
            print(informacion)

            
            paraquien = informacion['receptor']
            textoMensaje = informacion['mensaje']
            

            mensaje1 = Mensaje(enviar=(usuario), recibir = (paraquien), mensaje=textoMensaje, leido = False)
            mensaje1.save()
            return render(request, 'mensajes/mensajeFormulario.html', {"form": form, "alerta": "mensaje enviado"} )
        else:
            return render(request, 'mensajes/home.html', {"alerta": "pailas"} )
    else:
        formulario = MensajeForm()
       
    return render(request, 'mensajes/mensajeFormulario.html', {"form": formulario} )
# pruebas
# def leerMensaje(request, enviar, recibir):
#     if request.method == "GET":
#         return render(request, "leerMensaje.html",
#                       {'users': User.objects.exclude(username=request.user.username),
#                        'receptor': User.objects.get(id=recibir),
#                        'mensaje': Mensaje.objects.filter(enviar_id=enviar, recibir_id=recibir) |
#                                    Mensaje.objects.filter(enviar_id=enviar, recibir_id=enviar)})
def leerMensaje(request):
    usuario = request.user
    ver = Mensaje.objects.filter(recibir = usuario)
    for mensaje in ver:
        mensaje.leido = True
        mensaje.save()
    print(ver)
    
    return render(request, "mensajes/leerMensaje.html", {"mensajes": ver})

def enviadoMensaje(request):
    usuario = request.user
    ver = Mensaje.objects.filter(enviar = usuario)
    print(ver)
    
    return render(request, "mensajes/enviadoMensaje.html", {"mensajes": ver})

def buscarMensaje(request):
    pass

def mensajeUsuarios(request):
   
    if request.method == "GET":
        return render(request, 'mensajes/mensajeUsuarios.html',
                      {'users': User.objects.exclude(username=request.user.username)})
