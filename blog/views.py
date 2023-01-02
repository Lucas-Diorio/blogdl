from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def inicio(request):
    return render(request, "blog/inicio.html")

def aboutme(request):
    return render(request, "blog/aboutme.html")