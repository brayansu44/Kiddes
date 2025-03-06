from django.db import models
from usuarios.models import PerfilUsuario

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
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="locales")
    nombre = models.CharField(max_length=100)

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

class Producto(models.Model):
    ESTADO_CHOICES = [
        ('Disponible', 'Disponible'),
        ('No disponible', 'No disponible'),
    ]

    referencia = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    color = models.CharField(max_length=50)
    talla = models.CharField(max_length=10)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='Disponible')

    def __str__(self):
        return f"{self.referencia} - {self.color} - {self.talla}"

class InventarioLocal(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE, related_name="inventario")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="stock_locales")
    cantidad_disponible = models.IntegerField()
    fecha_actualizacion = models.DateField(auto_now=True)
    stock_minimo = models.IntegerField()

    def __str__(self):
        return f"{self.local.nombre} - {self.producto.referencia} - {self.cantidad_disponible} uds"    
