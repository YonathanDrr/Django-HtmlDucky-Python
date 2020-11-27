from __future__ import unicode_literals

from django.db import models
#from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Region(models.Model) :
    idregion = models.IntegerField(null=False,primary_key=True,verbose_name="IdRegion")
    nombre = models.CharField( max_length=100)
    class Meta:
        db_table ='region'

    
    def __str__(self) : #Python3
        return self.nombre
 

class Comuna(models.Model) :
    idcomuna = models.CharField( max_length=100)
    nombre = models.CharField( max_length=100)
    idregion = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name="IdRegion")
    
    class Meta:
        db_table ='comuna'

    def __str__(self):
        return self.nombre


class Sucursale(models.Model):
    nombre = models.CharField( max_length=50,null=False)
    direccion = models.CharField( max_length=50,null=False)
    telefono = models.CharField( max_length=13,null=False)
    email = models.CharField( max_length=50,null=False)
    idcomuna = models.ForeignKey(Comuna, on_delete=models.CASCADE,null=False)


    class Meta:
        db_table ='sucursale'

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    titulo = models.CharField( max_length=50)
    descripcion = models.TextField( max_length=200,null=True)
    anio = models.CharField( max_length=50,verbose_name="año")
    precio = models.IntegerField(default=10000 ,editable=False) 
    idAutor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    email = models.CharField( max_length=50,null=True)
    imagen = models.ImageField(upload_to="curso", null=True)
    idSucursal = models.ForeignKey(Sucursale, on_delete=models.CASCADE,null=False)

    
    class Meta:
        db_table = 'curso'

    def __str__(self) : #Python 3 
        return self.titulo +'   ' + 'Creado por ' + self.idAutor.username 

class Compra(models.Model):
    idCurso = models.ForeignKey(Curso,on_delete=models.PROTECT,verbose_name='Curso')
    idAutor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,verbose_name='Comprador')
    class Meta:
        db_table = 'compra'

    
    def __str__(self) : #Python 3 
        return self.idCurso.titulo +'   ' + 'Comprado por ' + self.idAutor.username 

    



    