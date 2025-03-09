from django.contrib import admin

from .models import Proveedor
# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('UserResponsable', 'Razon_Social', 'Tipo_documento', 'Idientificacion', 'Telefono', 'Correo', 'Ciudad', 'Direccion', 'Fecha_Inicio_Actividad')
    search_fields = ('Razon_Social', 'Idientificacion')
    list_filter = ()


admin.site.register(Proveedor, ProveedorAdmin)