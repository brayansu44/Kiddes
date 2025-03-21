from django.contrib import admin
<<<<<<< HEAD
from .models import Ingresos_Producto, Salidas_Producto, Unidad_Medida, Tipo_insumo, Insumo, Ingresos_insumo, Uso_Insumo
# Register your models here.

#@admin.register(Ingresos_ProductoAdmin)
class Ingresos_ProductoAdmin(admin.ModelAdmin):
    list_display = ('Fecha', 'ProductoID', 'ProveedorID', 'Cantidad', 'UserResponsable', 'Estado')
    search_fields = ('ProductoID', 'UserResponsable')
    list_filter = ()

    #@admin.register(Salidas_ProductoAdmin)
class Salidas_ProductoAdmin(admin.ModelAdmin):
    list_display = ('Fecha', 'ProductoID', 'ProveedorID', 'Cantidad', 'UserResponsable', 'Estado', 'LocalID')
    search_fields = ('ProductoID', 'UserResponsable', 'LocalID')
    list_filter = ()

    #@admin.register(Unidad_MedidaAdmin)
class Unidad_MedidaAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)
    search_fields = ()
    list_filter = ()

    #@admin.register(Tipo_insumoAdmin)
class Tipo_insumoAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)
    search_fields = ()
    list_filter = ()

    #@admin.register(InsumoAdmin)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Tipo_insumoID', 'Unidad_MedidaID', 'Cantidad', 'Estado')
    search_fields = ()
    list_filter = ()

    #@admin.register(Ingresos_insumoAdmin)
class Ingresos_insumoAdmin(admin.ModelAdmin):
    list_display = ("InsumoID", "Fecha", "Cantidad", "ProveedorID", "UserResponsable")
    search_fields = ('InsumoID', 'UserResponsable')
    list_filter = ()

    #@admin.register(Uso_InsumoAdmin)
class Uso_InsumoAdmin(admin.ModelAdmin):
    list_display = ('InsumoID', 'ProductoID', 'Fecha', 'Cantidad', 'Observaciones_Destino', 'UserResponsable')
    search_fields = ('InsumoID', 'UserResponsable')
    list_filter = ()

admin.site.register(Ingresos_Producto, Ingresos_ProductoAdmin)  
admin.site.register(Salidas_Producto, Salidas_ProductoAdmin)
admin.site.register(Unidad_Medida, Unidad_MedidaAdmin)
admin.site.register(Tipo_insumo, Tipo_insumoAdmin)
admin.site.register(Insumo, InsumoAdmin)
admin.site.register(Ingresos_insumo, Ingresos_insumoAdmin)
admin.site.register(Uso_Insumo, Uso_InsumoAdmin)
=======
from .models import (
    EntregaCorte, Stock, SalidaProducto, ConfirmacionRecepcion, 
    UnidadMedida, TipoInsumo, Insumo, IngresoInsumo, UsoInsumo
)

@admin.register(EntregaCorte)
class EntregaCorteAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'producto', 'cantidad', 'user_responsable')
    list_filter = ('fecha', 'user_responsable')
    search_fields = ('producto__producto__nombre',)  # Búsqueda por nombre del producto
    date_hierarchy = 'fecha'

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('producto_variante', 'cantidad')
    search_fields = ('producto_variante__producto__nombre',)

@admin.register(SalidaProducto)
class SalidaProductoAdmin(admin.ModelAdmin):
    list_display = ("producto", "cantidad", "local", "estado", "fecha")
    list_filter = ("estado", "local")

@admin.register(ConfirmacionRecepcion)
class ConfirmacionRecepcionAdmin(admin.ModelAdmin):
    list_display = ("salida", "user_encargado", "confirmado", "fecha_confirmacion")
    list_filter = ("confirmado",)
    actions = ["confirmar_recepcion"]

    def save_model(self, request, obj, form, change):
        if obj.confirmado and not obj.user_encargado:
            obj.user_encargado = request.user.perfilusuario  # Asigna el usuario logueado
        super().save_model(request, obj, form, change)

    @admin.action(description="Confirmar recepción")
    def confirmar_recepcion(self, request, queryset):
        for recepcion in queryset:
            if not recepcion.confirmado:
                recepcion.confirmado = True
                recepcion.user_encargado = request.user.perfilusuario  # Asigna usuario autenticado
                recepcion.save()

    confirmar_recepcion.short_description = "Confirmar recepción de productos"


@admin.register(UnidadMedida)
class UnidadMedidaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(TipoInsumo)
class TipoInsumoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_insumo', 'unidad_medida', 'cantidad')
    list_filter = ('tipo_insumo', 'unidad_medida')
    search_fields = ('nombre',)

@admin.register(IngresoInsumo)
class IngresoInsumoAdmin(admin.ModelAdmin):
    list_display = ('insumo', 'fecha', 'cantidad', 'proveedor', 'user_responsable', 'estado')
    list_filter = ('estado', 'fecha', 'proveedor')
    search_fields = ('insumo__nombre', 'proveedor__nombre')
    actions = ['marcar_como_completado']

    @admin.action(description="Marcar como Completado")
    def marcar_como_completado(self, request, queryset):
        queryset.update(estado='Completado')

@admin.register(UsoInsumo)
class UsoInsumoAdmin(admin.ModelAdmin):
    list_display = ('insumo', 'producto', 'fecha', 'cantidad', 'uso_destino', 'user_responsable')
    list_filter = ('uso_destino', 'fecha')
    search_fields = ('insumo__nombre', 'producto__producto__nombre')
>>>>>>> 0143c21 (nuevos cabios en el modulo de bodega)
