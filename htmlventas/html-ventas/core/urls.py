from django.urls import path,include
from .views import HomePageView, SamplePageView , Inicio,MisCompras,CompraDetailView,CursoViewSet
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Cursos',CursoViewSet)

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
    path('inicio/',views.Inicio, name = 'inicio'),
    path('MisCompras/',views.MisCompras, name ='MisCompras'),
    #path('DetalleCompras/',views.DetalleCompras, name ='DetalleCompras'),
   # path('<id>/', CompraDetailView.as_view(), name='detailCompra'),

    path('api/', include(router.urls) ),
    #path('mantenedor/', include('mantenedor.urls')),

]

