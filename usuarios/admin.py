from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, PerfilUsuario, Cargo, Area, Empresa

# Register your models here.

class UsuarioAdmin(UserAdmin):
    list_display = ('email', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'username')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'documento')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class CargoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'area')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class AreaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'empresa')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'razon_social', 'nit', 'telefono', 'correo', 'fecha_inicio_actividad', 'usuario']
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()          

admin.site.register(Usuario, UsuarioAdmin)  
admin.site.register(PerfilUsuario, PerfilUsuarioAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Empresa, EmpresaAdmin) 