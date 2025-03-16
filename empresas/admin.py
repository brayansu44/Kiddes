from django.contrib import admin
from django.utils.html import format_html
from .models import Empresa, Area, DiasFuncionamiento, Local, InventarioLocal

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("razon_social", "nit", "telefono", "correo", "mostrar_logo")
    search_fields = ("razon_social", "nit", "correo")
    
    def mostrar_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;" />', obj.logo.url)
        return "(Sin logo)"
    
    mostrar_logo.short_description = "Logo"

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "empresa", "descripcion")
    search_fields = ("nombre", "empresa__razon_social")

@admin.register(DiasFuncionamiento)
class DiasFuncionamientoAdmin(admin.ModelAdmin):
    list_display = ("dia", "get_dia_display")
    ordering = ("dia",)

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ("nombre", "empresa", "telefono", "direccion", "mostrar_horario")
    search_fields = ("nombre", "empresa__razon_social", "direccion")
    filter_horizontal = ("Horario_habil",)

    def mostrar_horario(self, obj):
        return ", ".join([dia.get_dia_display() for dia in obj.Horario_habil.all()])
    
    mostrar_horario.short_description = "Días de funcionamiento"

@admin.register(InventarioLocal)
class InventarioLocalAdmin(admin.ModelAdmin):
    list_display = ('local', 'variante', 'entradas', 'salidas', 'stock_actual')
    list_filter = ('local', 'variante__producto', 'fecha')  
    search_fields = ('local__nombre', 'variante__producto__referencia', 'variante__color__nombre', 'variante__talla__nombre')
    ordering = ('-fecha',)
    readonly_fields = ('stock_actual', 'fecha') 

    fieldsets = (
        ('Información del Local', {
            'fields': ('local', 'variante')
        }),
        ('Movimientos de Stock', {
            'fields': ('entradas', 'salidas', 'stock_actual')
        }),
        ('Fecha de Registro', {
            'fields': ('fecha',)
        }),
    )

