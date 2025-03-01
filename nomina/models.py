from django.db import models

# Create your models here.
from django.db import models
from usuarios.models import PerfilUsuario, Empresa, Area, Account

# Modelos locales
class Devengado(models.Model):
    UsuarioID           = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    Auxilio_Transporte  = models.FloatField()
    Exonerado_Aportes   = models.FloatField()
    Dias                = models.IntegerField(unique=True)
    Salario             = models.FloatField()
    Horas_Extras        = models.IntegerField(unique=True)
    Recargos_Nocturnos  = models.IntegerField(unique=True)
    Recargos_Domical    = models.IntegerField(unique=True)
    Total               = models.FloatField()


class Deducciones(models.Model):
    UsuarioID   = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    Salud       = models.FloatField()
    Pension     = models.FloatField()
    Fondo       = models.FloatField()
    Retencion   = models.FloatField()
    Otros       = models.FloatField()

class Provisiones(models.Model):
    EmpresaID           = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    Pension             = models.FloatField()
    Salud               = models.FloatField()
    Riesgo_Laboral      = models.FloatField()
    SENA                = models.FloatField()
    ICBF                = models.FloatField()
    Caja_Compensacion   = models.FloatField()
    Prima               = models.FloatField()
    Cesantias           = models.FloatField()
    Interes_Cesantias   = models.FloatField()
    Vacaciones          = models.FloatField()
    Total               = models.FloatField()


class AportesParafiscal(models.Model):
    UsuarioID           = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    SENA                = models.FloatField()
    ICBF                = models.FloatField()
    Caja_Compensacion   = models.FloatField()
    Aporte_Salud        = models.FloatField()

class Aprobador(models.Model):
    UsuarioiID          = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    EmpresaID           = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    Observaciones       = models.CharField(max_length=100)

class Comprobante(models.Model):
    Fecha           = models.DateField(auto_now_add=True)
    NomnaID         = models.ForeignKey("Nomina", on_delete=models.CASCADE)
    Observaciones   = models.CharField(max_length=100)
    UsuarioiID      = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    EmpresaID       = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    AreaID          = models.ForeignKey(Area, on_delete=models.CASCADE)
    UserResponsable = models.ForeignKey(Account, on_delete=models.CASCADE)
    AprobadorID     = models.ForeignKey(Aprobador, on_delete=models.CASCADE)

# Modelo Nomina
class Nomina(models.Model):
    Periodo_pago        = models.DateField(auto_now_add=True)
    Fecha_liquidacion   = models.DateField(auto_now_add=True)
    UsuarioID           = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    DevengadoID         = models.ForeignKey(Devengado, on_delete=models.CASCADE)
    DeduccionesID       = models.ForeignKey(Deducciones, on_delete=models.CASCADE)
    ProvisionesID       = models.ForeignKey(Provisiones, on_delete=models.CASCADE)
    Aportes_ParafiscalID= models.ForeignKey(AportesParafiscal, on_delete=models.CASCADE)
    ComprobanteID       = models.ForeignKey(Comprobante, on_delete=models.CASCADE)
    Neto_Pagado         = models.FloatField()

    def _str_(self):
        return f'Nomina {self.id} - {self.UsuarioID.nombre}'