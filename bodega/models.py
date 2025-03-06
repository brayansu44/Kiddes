from django.db import models

# Create your models here.
#from usuarios.models import Empresa, Usuario
#from Producto.models import Producto, Stock, Proveedor

# Modelos locales
class Ingresos_Producto(models.Model):
    Fecha           = models.DateField(null=False, blank=False)
    ProductoID      = models.ForeignKey("Producto.Producto", on_delete=models.CASCADE)
    ProveedorID     = models.ForeignKey("Producto.Proveedor", on_delete=models.CASCADE)
    Cantidad        = models.IntegerField(null=False, blank=False)
    UserResponsable = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)
    Estados = (
        ('Activo', 'Active'),
        ('Inactivo', 'Inactive'),
    )
    Estado          = models.CharField(max_length=50, choices=Estados, default='Activo')

class Local(models.Model):
    Nombre    = models.CharField(max_length=100, unique=True, null=False, blank=False)
    Horario   = models.CharField(max_length=100)
    Telefono  = models.IntegerField(unique=True)
    Direccion = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'

class Salidas_Producto(models.Model):
    Fecha           = models.DateField(null=False, blank=False)
    ProductoID      = models.ForeignKey("Producto.Producto", on_delete=models.CASCADE)
    ProveedorID     = models.ForeignKey("Producto.Proveedor", on_delete=models.CASCADE)
    Cantidad        = models.IntegerField(null=False, blank=False)
    UserResponsable = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)
    Estados = (
        ('Activo', 'Active'),
        ('Inactivo', 'Inactive'),
    )
    Estado          = models.CharField(max_length=50, choices=Estados, default='Activo')
    LocalID         = models.ForeignKey(Local, on_delete=models.CASCADE)

class Unidad_Medida(models.Model):
    Nombre    = models.CharField(max_length=100, unique=True, null=False, blank=False)

class Tipo_insumo(models.Model):
    Nombre    = models.CharField(max_length=100, unique=True, null=False, blank=False)

class Insumo(models.Model):
    Nombre          = models.CharField(max_length=100, unique=True, null=False, blank=False)
    Tipo_insumoID   = models.ForeignKey(Tipo_insumo, on_delete=models.CASCADE)
    Unidad_MedidaID = models.ForeignKey(Unidad_Medida, on_delete=models.CASCADE)
    Cantidad        = models.IntegerField(null=False, blank=False)
    Estados = (
        ('Activo', 'Active'),
        ('Inactivo', 'Inactive'),
    )
    Estado          = models.CharField(max_length=50, choices=Estados, default='Activo')

class Ingresos_insumo(models.Model):
    InsumoID        = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    Fecha           = models.DateField(null=False, blank=False)
    Cantidad        = models.IntegerField(null=False, blank=False)
    ProveedorID     = models.ForeignKey("Producto.Proveedor", on_delete=models.CASCADE)
    UserResponsable = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)

class Uso_Insumo(models.Model):
    InsumoID        = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    ProductoID      = models.ForeignKey("Producto.Producto", on_delete=models.CASCADE)
    Fecha           = models.DateField(null=False, blank=False)
    Cantidad        = models.IntegerField(null=False, blank=False)
    Observaciones_Destino = models.CharField(max_length=100)
    UserResponsable = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)