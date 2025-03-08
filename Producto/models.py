from django.db import models

# Create your models here.
from usuarios.models import Usuario
from empresas.models import Empresa
from bodega.models import Ingresos_Producto, Salidas_Producto

# Modelos locales
class Proveedor(models.Model):
    UserResponsable       = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Razon_Social          = models.CharField(max_length=100, null=False, blank=False)
    Tipo_documentos=(
        ('C.C.','C.C'),
        ('NIT.','NIT.'),
        ('PAS','PAS'),
    )
    Tipo_documento        = models.CharField(max_length=50, choices=Tipo_documentos, default='NIT')
    Idientificacion       = models.IntegerField(unique=True, null=False, blank=False)
    Telefono              = models.IntegerField()
    Correo                = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    Ciudad                = models.CharField(max_length=100)
    Direccion             = models.CharField(max_length=100)
    Fecha_Inicio_Actividad= models.DateField(null=False, blank=False)
    
    class Meta:
        verbose_name='Proveedor'
        verbose_name_plural='Proveedor'


class Codigo(models.Model):
    Codigo  = models.IntegerField(unique=True, null=False, blank=False)

class Stock(models.Model):
    Producto        = models.ForeignKey("Producto", on_delete=models.CASCADE)
    Ingreso_Producto= models.ForeignKey(Ingresos_Producto, on_delete=models.CASCADE)
    Salida_Producto = models.ForeignKey(Salidas_Producto, on_delete=models.CASCADE)

    class Meta:
        verbose_name='Stock'
        verbose_name_plural='Stock'

class Producto(models.Model):
    CodigoID        = models.ForeignKey(Codigo, on_delete=models.CASCADE)
    EmpresaID       = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    Referencia      = models.CharField(max_length=100)
    Talla           = models.CharField(max_length=100)
    Color           = models.CharField(max_length=100)
    Descripcion     = models.CharField(max_length=100)
    Qty_Disponible  = models.IntegerField()
    StockID         = models.ForeignKey(Stock, on_delete=models.CASCADE)
    ESTADO_CHOICES = [
        ('Disponible', 'Disponible'),
        ('No disponible', 'No disponible'),
    ]
    Diseno          = models.CharField(max_length=100)
    Precio_venta    = models.FloatField()
    Descuento       = models.FloatField()
    Garantia        = models.IntegerField()

    def __str__(self):
        return f"{self.referencia} - {self.color} - {self.talla}"



