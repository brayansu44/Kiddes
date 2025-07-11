from django.db import models
from proveedores.models import Proveedor

# Create your models here.

# Modulo de cuentas por cobrar
class Cliente(models.Model):
    identificacion = models.IntegerField(unique=True, null=False, blank=False, default='0')
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField(blank=True)
    direccion = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre

class FacturaVenta(models.Model):
    numero_factura      = models.CharField(max_length=20)
    cliente             = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_emision       = models.DateField(auto_now_add=True)
    fecha_vencimiento   = models.DateField()
    monto_total         = models.FloatField(blank=True)
    saldo_pendiente     = models.FloatField()

    def actualizar_saldo(self):
        pagos = self.pagorecibido_set.aggregate(models.Sum('monto_pagado'))['monto_pagado__sum'] or 0
        self.saldo_pendiente = self.monto_total - pagos
        self.save()

    def __str__(self):
        return f"Factura {self.numero_factura} - {self.cliente.nombre}"

    class Meta:
        verbose_name = "Factura de Venta"
        verbose_name_plural = "Facturas de Venta"

class PagoRecibido(models.Model):
    METODOS_PAGO = [
        ('Efectivo', 'Efectivo'),
        ('Transferencia', 'Transferencia'),
        ('Tarjeta', 'Tarjeta de Crédito/Débito'),
    ]
    factura         = models.ForeignKey(FacturaVenta, on_delete=models.CASCADE)   
    monto_pagado    = models.FloatField()
    fecha_pago      = models.DateField(auto_now_add=True)
    metodo_pago     = models.CharField(max_length=50, choices=METODOS_PAGO)
    observaciones   = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.factura.actualizar_saldo()

    def __str__(self):
        return f"Pago {self.monto_pagado} - {self.factura.numero_factura}"

    class Meta:
        verbose_name = "Pago Recibido"
        verbose_name_plural = "Pagos Recibidos"

# Modulo de cuentas por pagar
class FacturaCompra(models.Model):
    numero_factura      = models.CharField(max_length=20)
    proveedor           = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_emision       = models.DateField(auto_now_add=True)
    fecha_vencimiento   = models.DateField()
    monto_total         = models.FloatField(blank=True)
    saldo_pendiente     = models.FloatField()

    def __str__(self):
        return f"Factura {self.numero_factura} - {self.proveedor.nombre}"

    class Meta:
        verbose_name = "Factura de Compra"
        verbose_name_plural = "Facturas de Compra"   

class Pago(models.Model):
    METODOS_PAGO = [
        ('Efectivo', 'Efectivo'),
        ('Transferencia', 'Transferencia'),
        ('Tarjeta', 'Tarjeta de Crédito/Débito'),
    ]
    factura         = models.ForeignKey(FacturaCompra, on_delete=models.CASCADE)   
    monto_pagado    = models.FloatField()
    fecha_pago      = models.DateField(auto_now_add=True)
    metodo_pago     = models.CharField(max_length=50, choices=METODOS_PAGO)
    observaciones   = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.factura.actualizar_saldo()

    def __str__(self):
        return f"Pago {self.monto_pagado} - {self.factura.numero_factura}"

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"   