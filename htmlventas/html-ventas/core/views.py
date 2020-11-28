from django.views.generic.base import TemplateView
from django.shortcuts import render,redirect
from.models import Curso,Compra
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

#REST_FRAMEWORK
from rest_framework import viewsets
from.serializers import CursoSerializers

#STRIPE
import stripe
stripe.api_key='sk_test_51HsGjSEyhh4JF78jovdaiKr4lXSG2cXrmRa8YTUFo0xehrsnd6SQJJrlcnHttUexLCuNwctpjy0scosQsVKStziG00DTmryxqm'

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



class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers


#Pagos con Stripe

def compra(request):
    cursos = Curso.objects.all()
    data = {
        'cursos' : cursos
    }
    return render(request,'core/Compras/compraCurso.html',data)    

def cargo(request):
    if request.POST:
        precio = request.POST["precio"]
    redirect('Gracias !')

def gracias(request):
    render(request,'core/Compras/gracias.html')