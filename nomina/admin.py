from django.contrib import admin
from .models import Devengado, Deducciones, Provisiones, AportesParafiscal, Aprobador, Comprobante, Nomina, EPS, ARL, Pension, Caja_Compensacion

#@admin.register(Devengado)
class DevengadoAdmin(admin.ModelAdmin):
    list_display = ('UsuarioID', 'Auxilio_Transporte', 'Exonerado_Aportes', 'Dias', 'Salario', 'Horas_Extras', 'Recargos_Nocturnos', 'Recargos_Domical', 'Total')
    search_fields = ()
    list_filter = ()

#@admin.register(Deducciones)
class DeduccionesAdmin(admin.ModelAdmin):
    list_display = ('UsuarioID', 'Salud', 'Pension', 'Fondo', 'Retencion', 'Otros')
    search_fields = ()
    list_filter = ()

#@admin.register(Provisiones)
class ProvisionesAdmin(admin.ModelAdmin):
    list_display = ('EmpresaID', 'Pension', 'Salud', 'Riesgo_Laboral', 'SENA', 'ICBF', 'Caja_Compensacion', 'Prima', 'Cesantias', 'Interes_Cesantias', 'Vacaciones', 'Total')
    search_fields = ()
    list_filter = ()

#@admin.register(AportesParafiscal)
class AportesParafiscalAdmin(admin.ModelAdmin):
    list_display = ('UsuarioID', 'SENA', 'ICBF', 'Caja_Compensacion', 'Aporte_Salud')
    search_fields = ()
    list_filter = ()

#@admin.register(Aprobador)
class AprobadorAdmin(admin.ModelAdmin):
    list_display = ('UsuarioiID', 'EmpresaID', 'Observaciones')
    search_fields = ('UsuarioiID', 'EmpresaID')
    list_filter = ()

#@admin.register(Comprobante)
class ComprobanteAdmin(admin.ModelAdmin):
    list_display = ('Fecha', 'NomnaID', 'Observaciones', 'UsuarioiID', 'EmpresaID', 'AreaID', 'UserResponsable', 'AprobadorID')
    search_fields = ('UsuarioiID', 'EmpresaID', 'AreaID', 'UserResponsable')
    list_filter = ()

#@admin.register(Nomina)
class NominaAdmin(admin.ModelAdmin):
    list_display = ('Periodo_pago', 'Fecha_liquidacion', 'UsuarioID', 'DevengadoID', 'DeduccionesID', 'ProvisionesID', 'Aportes_ParafiscalID', 'ComprobanteID', 'Neto_Pagado')
    search_fields = ('UsuarioID', 'Periodo_pago')
    list_filter = ()

#@admin.register(EPS)
class EPSAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Direccion', 'Telefono', 'correo')
    search_fields = ()
    list_filter = ()

#@admin.register(ARL)
class ARLAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Direccion', 'Telefono', 'correo')
    search_fields = ()
    list_filter = ()

#@admin.register(Pension)
class PensionAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Direccion', 'Telefono', 'correo')
    search_fields = ()
    list_filter = ()

#@admin.register(Caja_Compensacion)
class Caja_CompensacionAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Direccion', 'Telefono', 'correo')
    search_fields = ()
    list_filter = ()

admin.site.register(Devengado, DevengadoAdmin)  
admin.site.register(Deducciones, DeduccionesAdmin)
admin.site.register(Provisiones, ProvisionesAdmin)
admin.site.register(AportesParafiscal, AportesParafiscalAdmin)
admin.site.register(Aprobador, AprobadorAdmin)
admin.site.register(Comprobante, ComprobanteAdmin)
admin.site.register(Nomina, NominaAdmin)
admin.site.register(EPS, EPSAdmin)
admin.site.register(ARL, ARLAdmin)
admin.site.register(Pension, PensionAdmin)
admin.site.register(Caja_Compensacion, Caja_CompensacionAdmin)
