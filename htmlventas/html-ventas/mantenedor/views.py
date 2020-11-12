from django.shortcuts import render, redirect
from django.http import HttpResponse

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
from core.models import Curso,Compra
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
 
from django import forms



def index(request):
 
    return render(request,"mantenedor/index.html")

def producto(request):
    cursos = Curso.objects.all()
    data = {
        'cursos' : cursos
    }
    return render(request,"mantenedor/Productos/FrCurso.html",data)

def modelo(request):
    return render(request,"mantenedor/Productos/FrDetalle.html")

def marca(request):
    return render(request,"mantenedor/Productos/FrSucursal.html")


 