from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Empresa, Area, Local, DiasFuncionamiento, InventarioLocal

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "razon_social", "nit", "telefono", "correo")
    search_fields = ("nombre", "nit")
    list_filter = ("razon_social",)

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "empresa")
    search_fields = ("nombre",)
    list_filter = ("empresa",)

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ("nombre", "empresa", "telefono", "direccion")
    search_fields = ("nombre", "empresa__nombre")
    list_filter = ("empresa",)

@admin.register(DiasFuncionamiento)
class DiasFuncionamientoAdmin(admin.ModelAdmin):
    list_display = ("local", "dia")
    list_filter = ("dia", "local")

@admin.register(InventarioLocal)
class InventarioLocalAdmin(admin.ModelAdmin):
    list_display = ("local", "producto", "cantidad_disponible", "fecha_actualizada", "qty_minimo")
    search_fields = ("local__nombre", "producto__Referencia")
    list_filter = ("local", "producto")
