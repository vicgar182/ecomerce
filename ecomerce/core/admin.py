from django.contrib import admin
from .models import Marca, Automovil, Producto  # importamos de models Marca y Automovil

# Register your models here.


class AutomovilAdmin(admin.ModelAdmin):
    list_display = ('patente', 'marca', 'anio', 'modelo', 'imagen')
    search_fields = ['patente', 'modelo'],
    list_filter = ('marca',)



admin.site.register(Marca)  # Registramos la marca
admin.site.register(Automovil, AutomovilAdmin)  # Registramos el modelo
admin.site.register(Producto)  # Registramos el producto
