from django.contrib import admin
from .models import Codigo, Stock, Producto
# Register your models here.

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
    list_display = ('CodigoID', 'Referencia', 'Talla', 'Color', 'Descripcion', 'Qty_Disponible', 'StockID', 'Estado', 'Diseno', 'Precio_venta', 'Descuento', 'Garantia')
    search_fields = ('CodigoID',)
    list_filter = ()

admin.site.register(Codigo, CodigoAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Producto, ProductoAdmin)