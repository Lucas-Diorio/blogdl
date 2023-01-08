from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('aboutme/', aboutme, name="aboutme"),
    path('addpost/', add_post, name="addpost"),
    path("post/<id>", post, name = "post"),
    path('buscarpost/', buscarPost, name="buscarpost"),
]
