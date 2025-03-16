from usuarios.models import PerfilUsuario
from empresas.models import Empresa

def global_context(request):
    perfil = None
    if request.user.is_authenticated:
        perfil = PerfilUsuario.objects.filter(usuario=request.user).first()
        empresas = Empresa.objects.all()
    
    return {
        'perfil': perfil,
        'empresas': empresas,
    }