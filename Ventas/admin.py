from django.contrib import admin
from .models import Ventas, Inventario_Local
# Register your models here.

#@admin.register(VentasAdmin)
class VentasAdmin(admin.ModelAdmin):
    list_display = ('LocalID', 'Factura', 'Fecha', 'ClienteID')
    search_fields = ('LocalID', 'ClienteID')
    list_filter = ()

#@admin.register(Inventario_LocalAdmin)
class Inventario_LocalAdmin(admin.ModelAdmin):
    list_display = ('LocalID', 'ProductoID', 'StockID', 'Fecha_Actualizada', 'Qty_Minimo')
    search_fields = ('LocalID', 'ProductoID')
    list_filter = ()


admin.site.register(Ventas, VentasAdmin)  
admin.site.register(Inventario_Local, Inventario_LocalAdmin)