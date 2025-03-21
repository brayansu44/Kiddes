<<<<<<< HEAD
from django.db import models
from proveedores.models import Proveedor
# Create your models here.


# Modelos locales
class Ingresos_Producto(models.Model):
    Fecha           = models.DateField(null=False, blank=False)
    ProductoID = models.ForeignKey("Producto.Producto", on_delete=models.CASCADE)
    ProveedorID     = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    Cantidad        = models.IntegerField(null=False, blank=False)
    UserResponsable = models.ForeignKey("usuarios.PerfilUsuario", on_delete=models.CASCADE)
    Estados = (
        ('Activo', 'Active'),
        ('Inactivo', 'Inactive'),
    )
    Estado          = models.CharField(max_length=50, choices=Estados, default='Activo')

class Salidas_Producto(models.Model):
    Fecha           = models.DateField(null=False, blank=False)
    ProductoID = models.ForeignKey("Producto.Producto", on_delete=models.CASCADE)
    ProveedorID     = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    Cantidad        = models.IntegerField(null=False, blank=False)
    UserResponsable = models.ForeignKey("usuarios.PerfilUsuario", on_delete=models.CASCADE)
    Estados = (
        ('Activo', 'Active'),
        ('Inactivo', 'Inactive'),
    )
    Estado          = models.CharField(max_length=50, choices=Estados, default='Activo')
    LocalID         = models.ForeignKey("empresas.InventarioLocal", on_delete=models.CASCADE)

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
    ProveedorID     = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    UserResponsable = models.ForeignKey("usuarios.PerfilUsuario", on_delete=models.CASCADE)

class Uso_Insumo(models.Model):
    InsumoID        = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    ProductoID      = models.ForeignKey("Producto.Producto", on_delete=models.CASCADE)
    Fecha           = models.DateField(null=False, blank=False)
    Cantidad        = models.IntegerField(null=False, blank=False)
    Observaciones_Destino = models.CharField(max_length=100)
    UserResponsable = models.ForeignKey("usuarios.PerfilUsuario", on_delete=models.CASCADE)
=======
from django.db import models, transaction
from proveedores.models import Proveedor
from Producto.models import ProductoVariante
from locales.models import InventarioLocal

class EstadoChoices(models.TextChoices):
    PENDIENTE = 'Pendiente', 'Pendiente'
    CONFIRMADO = 'Confirmado', 'Confirmado'
    CANCELADO = 'Cancelado', 'Cancelado'
    COMPLETADO = 'Completado', 'Completado'

class EntregaCorte(models.Model):
    fecha = models.DateField(auto_now_add=True)
    producto = models.ForeignKey(ProductoVariante, on_delete=models.CASCADE, related_name="ingresos")
    cantidad = models.PositiveIntegerField()
    user_responsable = models.ForeignKey("usuarios.PerfilUsuario", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        with transaction.atomic(): 
            producto_bodega, created = Stock.objects.select_for_update().get_or_create(
                producto_variante=self.producto,
                defaults={'cantidad': self.cantidad} 
            )
            
            if not created:
                producto_bodega.cantidad += self.cantidad
                producto_bodega.save()

    def __str__(self):
        return f"Entrega Corte {self.cantidad} - {self.producto}"

class Stock(models.Model):
    producto_variante = models.OneToOneField(ProductoVariante, on_delete=models.CASCADE, related_name="bodega_stock")
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.producto_variante} - Stock: {self.cantidad}"

class SalidaProducto(models.Model):
    fecha = models.DateField(auto_now_add=True)
    producto = models.ForeignKey(ProductoVariante, on_delete=models.CASCADE, related_name="salidas")
    cantidad = models.PositiveIntegerField()
    user_responsable = models.ForeignKey("usuarios.PerfilUsuario", on_delete=models.CASCADE)
    local = models.ForeignKey("locales.InventarioLocal", on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, choices=EstadoChoices.choices, default=EstadoChoices.PENDIENTE)

    def save(self, *args, **kwargs):
        if self.pk is None:  
            stock, created = Stock.objects.get_or_create(producto_variante=self.producto)

            if stock.cantidad < self.cantidad:
                raise ValueError(f"No hay suficiente stock para la salida de {self.producto}. Stock disponible: {stock.cantidad}")

            stock.cantidad -= self.cantidad
            stock.save()

            super().save(*args, **kwargs)
            ConfirmacionRecepcion.objects.create(salida=self, confirmado=False)
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"Salida {self.cantidad} - {self.producto} - {self.local}"
    
from django.contrib.auth.models import User  # Importamos User

class ConfirmacionRecepcion(models.Model):
    salida = models.OneToOneField(SalidaProducto, on_delete=models.CASCADE, related_name="confirmacion")
    fecha_confirmacion = models.DateTimeField(auto_now_add=True)
    user_encargado = models.ForeignKey("usuarios.PerfilUsuario", on_delete=models.CASCADE, related_name="confirmaciones", null=True, blank=True)
    confirmado = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Obtenemos la solicitud si está presente

        if self.confirmado:
            if request and not self.user_encargado:
                self.user_encargado = request.user.perfilusuario  # Asigna el usuario autenticado
            
            self.salida.estado = EstadoChoices.CONFIRMADO
            self.salida.save()

            inventario_local, created = InventarioLocal.objects.get_or_create(
                local=self.salida.local.local,  
                variante=self.salida.producto,
                defaults={'entradas': 0, 'stock_actual': 0}
            )
            inventario_local.entradas += self.salida.cantidad
            inventario_local.stock_actual += self.salida.cantidad
            inventario_local.save()

        super().save(*args, **kwargs)

    def __str__(self):
        estado = "Confirmado" if self.confirmado else "Pendiente"
        return f"Recepción {estado} - {self.salida.producto} - {self.salida.local.local}"
 
 

class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

class TipoInsumo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

class Insumo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    tipo_insumo = models.ForeignKey(TipoInsumo, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

class IngresoInsumo(models.Model):
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, related_name="ingresos")
    fecha = models.DateField(auto_now_add=True)
    cantidad = models.PositiveIntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    user_responsable = models.ForeignKey("usuarios.PerfilUsuario", on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, choices=EstadoChoices.choices, default=EstadoChoices.COMPLETADO)

class UsoInsumo(models.Model):
    DESTINO_CHOICES = [
        ('Lavado', 'Lavado'),
        ('Costura', 'Costura'),
        ('Otros', 'Otros'),
    ]
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, related_name="usos")
    producto = models.ForeignKey(ProductoVariante, on_delete=models.CASCADE, related_name="insumos_usados")
    fecha = models.DateField(auto_now_add=True)
    cantidad = models.PositiveIntegerField()
    uso_destino = models.CharField(max_length=50, choices=DESTINO_CHOICES, default='Lavado')
    observaciones = models.TextField(null=True, blank=True)  # Cambiado de TimeField a TextField
    user_responsable = models.ForeignKey("usuarios.PerfilUsuario", on_delete=models.CASCADE)
>>>>>>> 0143c21 (nuevos cabios en el modulo de bodega)
