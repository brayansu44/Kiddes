from django.db import models

# Create your models here.
# Modelos locales
class Ventas(models.Model):
    LocalID     = models.ForeignKey("bodega.local", on_delete=models.CASCADE)
    Factura     = models.ForeignKey("Cuentas.FacturaVenta", on_delete=models.CASCADE)
    Fecha       = models.DateField(null=False, blank=False)
    ClienteID   = models.ForeignKey("Cuentas.Cliente", on_delete=models.CASCADE)

class Inventario_Local(models.Model):
    LocalID             = models.ForeignKey("bodega.local", on_delete=models.CASCADE)
    ProductoID          = models.ForeignKey("Producto.Producto", on_delete=models.CASCADE)
    StockID             = models.ForeignKey("Producto.Stock", on_delete=models.CASCADE)
    Fecha_Actualizada   = models.DateField(null=False, blank=False)
    Qty_Minimo          = models.IntegerField(unique=True, null=False, blank=False)