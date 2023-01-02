from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('aboutme', aboutme, name="aboutme"),
]
