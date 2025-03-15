from django.db import models
from deep_translator import GoogleTranslator

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Diseno(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    imagen = models.ImageField(upload_to='productos', blank=True)

    def __str__(self):
        return self.nombre
    
class Genero(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Color(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    nombre_en_ingles = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.nombre_en_ingles:  # Solo traducir si el campo está vacío
            self.nombre_en_ingles = GoogleTranslator(source='es', target='en').translate(self.nombre)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name='Color'
        verbose_name_plural='Colores'

    def __str__(self):
        return self.nombre
    
class Talla(models.Model):
    nombre = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre    

class Producto(models.Model):
    ESTADO_CHOICES = [
        ('Disponible', 'Disponible'),
        ('No disponible', 'No disponible'),
    ]

    TALLA_CHOICES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    ]

    codigo              = models.CharField(max_length=50, unique=True)
    referencia          = models.CharField(max_length=100)
    diseno              = models.ManyToManyField(Diseno, related_name="productos")
    color               = models.ManyToManyField(Color, related_name="productos")
    talla               = models.ManyToManyField(Talla, related_name="productos")
    categoria           = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name="productos")
    genero              = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, blank=True, related_name="productos")
    descripcion         = models.TextField(blank=True)
    estado              = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='Disponible')
    precio_venta        = models.DecimalField(max_digits=10, decimal_places=2)
    descuento           = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    garantia_meses      = models.PositiveIntegerField(default=0) 
    fecha_creacion      = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    @property
    def precio_final(self):
        return self.precio_venta * (1 - self.descuento / 100)

    def __str__(self):
        return f"{self.codigo} - {self.referencia} ({self.color}, {self.talla})"

