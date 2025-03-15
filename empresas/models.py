from django.db import models
from Producto.models import Producto

class Empresa(models.Model):
    nombre                  = models.CharField(max_length=100, unique=True)
    razon_social            = models.CharField(max_length=100)
    nit                     = models.CharField(max_length=20, unique=True)
    telefono                = models.CharField(max_length=20, unique=True)
    correo                  = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Area(models.Model):
    nombre      = models.CharField(max_length=100, unique=True, null=False, blank=False)
    descripcion = models.CharField(max_length=100)
    empresa     = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Local(models.Model):
    empresa     = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="locales")
    nombre      = models.CharField(max_length=100)
    telefono    = models.IntegerField()
    direccion   = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'

    def __str__(self):
        return f"{self.nombre} - {self.empresa.nombre}"

class DiasFuncionamiento(models.Model):
    DIAS_CHOICES = [
        (1, "Lunes"),
        (2, "Martes"),
        (3, "Miércoles"),
        (4, "Jueves"),
        (5, "Viernes"),
        (6, "Sábado"),
        (7, "Domingo"),
    ]
    
    local = models.ForeignKey(Local, on_delete=models.CASCADE, related_name="dias_funcionamiento")
    dia = models.IntegerField(choices=DIAS_CHOICES)

    def __str__(self):
        return f"{self.get_dia_display()} - {self.local.nombre}"

class InventarioLocal(models.Model):
    local                   = models.ForeignKey(Local, on_delete=models.CASCADE, related_name="inventario")
    producto                = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="stock_locales")
    cantidad_disponible     = models.PositiveIntegerField(default=0)
    fecha_actualizada       = models.DateField(auto_now=True)
    qty_minimo              = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.local.nombre} - {self.cantidad_disponible} uds - {self.producto}"

