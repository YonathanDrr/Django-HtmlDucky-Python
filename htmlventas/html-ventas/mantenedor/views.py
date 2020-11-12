from django.shortcuts import render, redirect
from django.http import HttpResponse

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
 
from django import forms



def index(request):
    return render(request,"mantenedor/index.html")

def producto(request):
    return render(request,"mantenedor/Productos/FrCurso.html")

def modelo(request):
    return render(request,"mantenedor/Productos/FrDetalle.html")

def marca(request):
    return render(request,"mantenedor/Productos/FrSucursal.html")


 