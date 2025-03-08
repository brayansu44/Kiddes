from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usuarios.models import PerfilUsuario

@login_required(login_url = 'login')
def home(request):
    perfil = PerfilUsuario.objects.filter(usuario=request.user).first()
    return render(request, 'home.html', {'perfil': perfil})