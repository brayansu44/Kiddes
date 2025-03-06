from django.contrib import admin
from .models import Proveedor, Codigo, Stock, Producto
# Register your models here.

#@admin.register(Caja_Compensacion)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('UserResponsable', 'Razon_Social', 'Tipo_documento', 'Idientificacion', 'Telefono', 'Correo', 'Ciudad', 'Direccion', 'Fecha_Inicio_Actividad')
    search_fields = ('UserResponsable', 'Idientificacion', 'Correo')
    list_filter = ()

    #@admin.register(Caja_Compensacion)
class CodigoAdmin(admin.ModelAdmin):
    list_display = ('Codigo',)
    search_fields = ()
    list_filter = ()

    #@admin.register(Caja_Compensacion)
class StockAdmin(admin.ModelAdmin):
    list_display = ('Producto', 'Ingreso_Producto', 'Salida_Producto')
    search_fields = ()
    list_filter = ()

    #@admin.register(Caja_Compensacion)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('CodigoID', 'EmpresaID', 'Referencia', 'Talla', 'Color', 'Descripcion', 'Qty_Disponible', 'StockID', 'Estado', 'Diseno', 'Precio_venta', 'Descuento', 'Garantia')
    search_fields = ('CodigoID', 'EmpresaID')
    list_filter = ()

admin.site.register(Proveedor, ProveedorAdmin)  
admin.site.register(Codigo, CodigoAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Producto, ProductoAdmin)