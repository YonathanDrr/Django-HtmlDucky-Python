from django.views.generic.base import TemplateView
from django.shortcuts import render
from.models import Curso,Compra
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



#Vistas basadas en clases

class HomePageView(TemplateView):
    template_name = "core/home2.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,{'title':"Ducky Cursos"})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"


#Vistas basadas en Funciones

def Inicio(request):
    cursos = Curso.objects.all()
    data = {
        'cursos' : cursos
    }
    return render(request,"core/home2.html",data) 

def MisCompras(request):
    compras = Compra.objects.all() 
    data = {
        'compras': compras
    }
    return render(request,"core/Compras/compras.html",data) 

def DetalleCompras(request):
    compras = Compra.objects.all() 
    data = {
        'compras': compras
    }
    return render(request,"core/Compras/comprasDetail.html",data) 


class CompraDetailView(DetailView):
    model = Compra
    template_name = 'core/Compras/comprasDetail.html'



