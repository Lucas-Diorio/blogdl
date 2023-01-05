from django.shortcuts import render
from blog.models import *

def aboutme(request):
    return render(request, "Página de Aboutme")

def inicio(request):
    posts = Post.objects.all().order_by('-id')[:4] # Consulta por id, y limita a 4 de mayor a menor (ORDER BY id DESC en SQL) (LIMIT 4)
    if len(posts) == 0:
        post_1 = Post.objects.none()
        post_2 = Post.objects.none()
        post_3 = Post.objects.none()
        post_4 = Post.objects.none()
    elif len(posts) == 1:
        post_1 = posts[0]
        post_2 = Post.objects.none()
        post_3 = Post.objects.none()
        post_4 = Post.objects.none()
    elif len(posts) == 2:
        post_1 = posts[0]
        post_2 = posts[1]
        post_3 = Post.objects.none()
        post_4 = Post.objects.none()
    elif len(posts) == 3:
        post_1 = posts[0]
        post_2 = posts[1]
        post_3 = posts[2]
        post_4 = Post.objects.none()
    else:     
        post_1 = posts[0]
        post_2 = posts[1]
        post_3 = posts[2]
        post_4 = posts[3]
    return render(request, "blog/inicio.html", {"blog_1": post_1, "blog_2": post_2, "blog_3": post_3, "blog_4": post_4})


# Post.objects.none() envia un queryset vacio