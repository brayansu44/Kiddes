from django.db import models
from django.core.exceptions import ValidationError
from Producto.models import ProductoVariante

class Empresa(models.Model):
    razon_social            = models.CharField(max_length=100)
    nit                     = models.CharField(max_length=20, unique=True)
    telefono                = models.CharField(max_length=20, unique=True)
    correo                  = models.EmailField(max_length=100, unique=True)
    logo                    = models.ImageField(upload_to='empresas', blank=True)

    def __str__(self):
        return self.razon_social

class Area(models.Model):
    nombre      = models.CharField(max_length=100, unique=True, null=False, blank=False)
    descripcion = models.CharField(max_length=100)
    empresa     = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre
    
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
    dia = models.IntegerField(choices=DIAS_CHOICES, unique=True)
 
    def __str__(self):
        return f"{self.get_dia_display()}" 

class Local(models.Model):
    empresa         = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="Empresa_relacionada")
    nombre          = models.CharField(max_length=100)
    telefono        = models.IntegerField()
    direccion       = models.CharField(max_length=255)
    Horario_habil   = models.ManyToManyField(DiasFuncionamiento, related_name="locales")

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'

    def __str__(self):
        return f"{self.nombre} - {self.empresa.razon_social}"
    
class InventarioLocal(models.Model):
    local               = models.ForeignKey(Local, on_delete=models.CASCADE, related_name="inventario")
    variante            = models.ForeignKey(ProductoVariante, on_delete=models.CASCADE, related_name="stock_locales")
    entradas            = models.PositiveIntegerField(default=0)
    salidas             = models.PositiveIntegerField(default=0)
    stock_actual        = models.PositiveIntegerField(default=0)
    fecha               = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('local', 'variante')
        verbose_name = 'Inventario Local'
        verbose_name_plural = 'Inventario Local'  

    def clean(self):
        if self.salidas > self.entradas:
            raise ValidationError({'salidas': 'Las salidas no pueden ser mayores que las entradas.'})

    def save(self, *args, **kwargs):
        self.stock_actual = self.entradas - self.salidas
        self.clean() 
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.local.nombre} - {self.variante} - Stock: {self.stock_actual} uds"



