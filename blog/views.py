from django.shortcuts import render
from blog.models import *
from blog.forms import *
from datetime import date
from django.contrib.auth.decorators import login_required
from usuarios.views import obtenerAvatar

def aboutme(request):
    return render(request, "Página de Aboutme")

def inicio(request):
    posts = Post.objects.all().order_by('-id')[:5] # Consulta por id, y limita a 5 de mayor a menor (ORDER BY id DESC en SQL) (LIMIT 5)
    if len(posts) == 0:
        post_1 = Post.objects.none()
        post_2 = Post.objects.none()
        post_3 = Post.objects.none()
        post_4 = Post.objects.none()
        post_5 = Post.objects.none()
    elif len(posts) == 1:
        post_1 = posts[0]
        post_2 = Post.objects.none()
        post_3 = Post.objects.none()
        post_4 = Post.objects.none()
        post_5 = Post.objects.none()
    elif len(posts) == 2:
        post_1 = posts[0]
        post_2 = posts[1]
        post_3 = Post.objects.none()
        post_4 = Post.objects.none()
        post_5 = Post.objects.none()
    elif len(posts) == 3:
        post_1 = posts[0]
        post_2 = posts[1]
        post_3 = posts[2]
        post_4 = Post.objects.none()
        post_5 = Post.objects.none()
    elif len(posts) == 4:
        post_1 = posts[0]
        post_2 = posts[1]
        post_3 = posts[2]
        post_4 = posts[3]
        post_5 = Post.objects.none()
    else:     
        post_1 = posts[0]
        post_2 = posts[1]
        post_3 = posts[2]
        post_4 = posts[3]
        post_5 = posts[4]
    return render(request, "usuarios/user.html", {"post_1": post_1, "post_2": post_2, "post_3": post_3, "post_4": post_4,"post_5": post_5, "avatar": obtenerAvatar(request)})


# Post.objects.none() envia un queryset vacio

def aboutme(request):
    return render(request, "aboutme.html", {"avatar": obtenerAvatar(request)})


def post(request, id):
    lectura_publicacion = Post.objects.get(id = id)
    return render(request, "post.html", {"lectura_publicacion" : lectura_publicacion, "avatar": obtenerAvatar(request)})

@ login_required
def add_post(request):
    if request.method == "POST":
        formulario = Form_Post(request.POST, request.FILES)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            nombre_autor = request.user.get_full_name()
            nueva_publicacion = Post(titulo = datos["titulo"], intro = datos["intro"], contenido = datos["contenido"], imagen = datos["imagen"] , autor = nombre_autor, fecha = date.today())
            nueva_publicacion.save()
            return render(request, "usuarios/user.html", {"mensaje": "El post ha sido agregado exitosamente!"})
        else:
            return render(request, "blog/addpost.html", {"form_post" : Form_Post(), "mensaje": "Intentelo Nuevamente, hubo un error"})
    else:
        return render(request, "blog/addpost.html", {"form_post" : Form_Post(), "mensaje": "Agregar un Post", "avatar": obtenerAvatar(request)})