from django.shortcuts import render, redirect
from django.http import HttpResponse

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
from core.models import Curso,Compra
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django import forms




def index(request):
 
    return render(request,"mantenedor/index.html")

def producto(request):
  
    return render(request,"mantenedor/Mgeneral/FrCurso.html")

def modelo(request):
    return render(request,"mantenedor/Mgeneral/FrDetalle.html")

def marca(request):
    return render(request,"mantenedor/Mgeneral/FrSucursal.html")

