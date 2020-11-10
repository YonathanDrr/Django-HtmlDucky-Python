from django.urls import path,include
from .views import HomePageView, SamplePageView , Inicio,MisCompras,CompraDetailView
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
    path('inicio/',views.Inicio, name = 'inicio'),
    path('MisCompras/',views.MisCompras, name ='MisCompras'),
    #path('DetalleCompras/',views.DetalleCompras, name ='DetalleCompras'),
   # path('<id>/', CompraDetailView.as_view(), name='detailCompra'),


    #path('mantenedor/', include('mantenedor.urls')),

]

