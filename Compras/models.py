from django.db import models

# Create your models here.
# Modelos locales
class Compras(models.Model):
    Fecha           = models.DateField(null=False, blank=False)
    ProveedorID     = models.ForeignKey("Producto.Proveedor", on_delete=models.CASCADE)
    UserResponsable = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)
    EmpresaID       = models.ForeignKey("Empresas.Empresa", on_delete=models.CASCADE)
    Factura         = models.ForeignKey("Cuentas.FacturaCompra", on_delete=models.CASCADE)

class Gastos_Operativos(models.Model):
    Fecha           = models.DateField(null=False, blank=False)
    Tipo_gasto      = models.CharField(max_length=50)
    Factura         = models.ForeignKey("Cuentas.FacturaCompra", on_delete=models.CASCADE)
    UserResponsable = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)
    Aprobador       = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)
    EmpresaID       = models.ForeignKey("Empresas.Empresa", on_delete=models.CASCADE)