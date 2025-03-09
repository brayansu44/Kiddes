from django.db import models
# Create your models here.
from usuarios.models import Usuario
from bodega.models import Ingresos_Producto, Salidas_Producto
from proveedores.models import Proveedor

class Codigo(models.Model):
    Codigo  = models.IntegerField(unique=True, null=False, blank=False)

class Stock(models.Model):
    Producto        = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    Ingreso_Producto= models.ForeignKey(Ingresos_Producto, on_delete=models.CASCADE)
    Salida_Producto = models.ForeignKey(Salidas_Producto, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Stock'
        verbose_name_plural='Stock'

class Producto(models.Model):
    ESTADO_CHOICES = [
        ('Disponible', 'Disponible'),
        ('No disponible', 'No disponible'),
    ]
    CodigoID        = models.ForeignKey(Codigo, on_delete=models.CASCADE)
    Referencia      = models.CharField(max_length=100)
    Talla           = models.CharField(max_length=100)
    Color           = models.CharField(max_length=100)
    Descripcion     = models.CharField(max_length=100)
    Qty_Disponible  = models.IntegerField()
    StockID         = models.ForeignKey(Stock, on_delete=models.CASCADE)
    Estado          = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='Disponible')
    Diseno          = models.CharField(max_length=100)
    Precio_venta    = models.FloatField()
    Descuento       = models.FloatField()
    Garantia        = models.IntegerField()

    def __str__(self):
        return f"{self.referencia} - {self.color} - {self.talla}"



