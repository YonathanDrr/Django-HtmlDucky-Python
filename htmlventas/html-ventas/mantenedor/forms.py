from django import forms
from django.forms import ModelForm
from core.models import Curso


class CursosForms(ModelForm):

    class Meta:
        model = Curso
        fields = ['titulo','descripcion','anio','idAutor','email','imagen','idSucursal']