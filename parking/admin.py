from django.contrib import admin

# Register your models here.
from .models import Plaza, Cliente, Dimensiones

@admin.register(Plaza)
class PlazaAdmin(admin.ModelAdmin):
    list_display = ('planta','numero')
    list_filter = ['planta']
    

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('dni','nombre', 'apellidos','vehiculo')
    fieldsets = (
        ('Datos personales',
        {'fields': [('dni','nombre', 'apellidos')]}), 
        ('Vehiculo',
        {'fields': [('vehiculo')]}) 
    )
    list_filter = ['nombre','apellidos']
    

@admin.register(Dimensiones)
class DimensionesAdmin(admin.ModelAdmin):
    list_display = ('tipo','anchura','largura')