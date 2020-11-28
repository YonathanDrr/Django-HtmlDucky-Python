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
from .forms import CursosForms



def index(request):
 
    return render(request,"mantenedor/index.html")

def ListarCursos(request):
    cursos = Curso.objects.all()
    data = {
        'cursos': cursos
    }
    return render(request,'mantenedor/Mgeneral/FrCurso.html',data)

def AgregarCursos(request):
    data = {
        'form' : CursosForms
    }
    if request.method == 'POST':
        formulario = CursosForms(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Curso Agregado exitosamente"
            
    return render(request,"mantenedor/Mgeneral/FrDetalle.html",data)

def marca(request):
    return render(request,"mantenedor/Mgeneral/FrSucursal.html")


