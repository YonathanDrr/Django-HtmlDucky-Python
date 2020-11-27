#Que es un serializador en Django envia y recibe datos unidirecionalmente
#bbdd -> datos-> JSON
#JSON -> datos -> bbdd

from rest_framework import serializers
from .models import Curso


class CursoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Curso
        fields =['titulo','descripcion','anio','idAutor','idSucursal']