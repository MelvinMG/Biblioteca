from django.contrib import admin
from .models import Perfil, Prestamo, historial_Multas,Libro, Revista, Tesis

# Register your models here.

admin.site.register(Perfil)
admin.site.register(Prestamo)
admin.site.register(historial_Multas)
admin.site.register(Libro)
admin.site.register(Revista)
admin.site.register(Tesis)
