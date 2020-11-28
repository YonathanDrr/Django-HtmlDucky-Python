from django.urls import path,include
from .views import HomePageView, SamplePageView , Inicio,MisCompras,CompraDetailView,CursoViewSet
from .import views
from rest_framework import routers

#Asignado variable para APIREST
router = routers.DefaultRouter()
router.register('Cursos',CursoViewSet)

urlpatterns = [
    #Urls Publicas
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
    path('inicio/',views.Inicio, name = 'inicio'),
    path('MisCompras/',views.MisCompras, name ='MisCompras'),
   
    #Urls de APIREST
    path('api/', include(router.urls) ),
   

    #Urls Compras
    path('compraCurso/', views.compra, name = 'Compras' ),
    path('cargo/', views.cargo, name = 'Cargo' ),
    path('gracias/', views.gracias, name= 'Gracias' ),


]

