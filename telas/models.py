from django.db import models
from usuarios.models import PerfilUsuario

# Create your models here.
class Tela(models.Model):
    nombre      = models.CharField(max_length=100, unique=True)
    color       = models.CharField(max_length=50)
    tipo        = models.CharField(max_length=50)
    proveedor   = models.CharField(max_length=100)
    ancho       = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return  f"{self.nombre} - {self.estado}"
    
class RolloTela(models.Model):
    ESTADO = (
        ('Completo', 'Completo'),
        ('Incompleto', 'Incompleto'),
    )
    tela            = models.ForeignKey(Tela, on_delete=models.CASCADE)
    largo_inicial   = models.DecimalField(max_digits=6, decimal_places=2)
    largo_restante  = models.DecimalField(max_digits=6, decimal_places=2)
    estado          = models.CharField(max_length=50, choices=ESTADO, default='Completo')

    def actualizar_estado(self):
        self.estado = 'Incompleto' if self.largo_restante < self.largo_inicial else 'Completo'
        self.save()

    def save(self, *args, **kwargs):
        self.actualizar_estado()
        super().save(*args, **kwargs)    

    def __str__(self):
        return f"{self.tela.nombre} - {self.estado}"
    
class OrdenProduccion(models.Model):
    fecha           = models.DateField(auto_now_add=True)
    referencia      = models.CharField(max_length=100, unique=True)
    cortador        = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, related_name="ordenes_produccion")
    total_unidades  = models.PositiveIntegerField()
    observaciones   = models.TextField(blank=True, null=True)

    def calcular_faltante(self):
        return max(0, self.rollo.largo_restante - self.largo_utilizado)

    def calcular_rendimiento(self):
        return self.largo_utilizado / self.rollo.largo_inicial * 100

    def save(self, *args, **kwargs):
        self.faltante_tela = self.calcular_faltante()
        self.rendimiento_rollo = self.calcular_rendimiento()
        self.rollo.largo_restante -= self.largo_utilizado
        self.rollo.save()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name='Orden Produccion'
        verbose_name_plural='Orden Produccion'

    def __str__(self):
        return f"Orden {self.referencia} - {self.total_unidades} unidades"    

class CorteTela(models.Model):
    orden               = models.ForeignKey(OrdenProduccion, on_delete=models.CASCADE, related_name="cortes")
    rollo               = models.ForeignKey(RolloTela, on_delete=models.CASCADE)
    largo_utilizado     = models.DecimalField(max_digits=6, decimal_places=2)
    capas_cortadas      = models.PositiveIntegerField()
    colas               = models.DecimalField(max_digits=6, decimal_places=2)
    faltante_tela       = models.DecimalField(max_digits=6, decimal_places=2)
    rendimiento_rollo   = models.DecimalField(max_digits=6, decimal_places=2)
    fecha_corte         = models.DateField(auto_now_add=True)
    responsable         = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Corte de {self.largo_utilizado}m - {self.rollo.tela.nombre}"
    
class TallaCorte(models.Model):
    TALLA = (
        ('S', 'Pequeño'),
        ('M', 'Mediano'),
        ('L', 'Grande'),
        ('XL', 'Extra Grande'),
    )
    corte       = models.ForeignKey(CorteTela, on_delete=models.CASCADE, related_name="tallas_cortes")
    talla       = models.CharField(max_length=2, choices=TALLA, default='S')
    cantidad    = models.PositiveIntegerField()

    def __str__(self):
        return f"Corte {self.corte.id} - Talla {self.talla} - {self.cantidad} unidades"        
    
class ComponentesTela(models.Model):
    TIPO_PIEZA = (
        ('Delantero', 'Delantero'),
        ('Posterior', 'Posterior'),
        ('Mangas', 'Mangas'),
        ('Cuellos', 'Cuellos'),
        ('Bolsillos', 'Bolsillos'),
    )
    talla_corte = models.ForeignKey(TallaCorte, on_delete=models.CASCADE, related_name="componentes_tela")
    tipo_pieza  = models.CharField(max_length=50, choices=TIPO_PIEZA, default='Delantero')
    cantidad    = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.tipo_pieza} - {self.cantidad} piezas para {self.talla_corte.talla}"

