from django.contrib import admin
from .models import Curso,Comuna,Sucursale
from registration.models import Profile
from core.models import Compra



# Register your models here.

 
admin.site.register(Curso)
admin.site.register(Comuna)
admin.site.register(Compra)
admin.site.register(Profile)
admin.site.register(Sucursale)

