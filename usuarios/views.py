from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import LoginForm

# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            remember_me = request.POST.get('remember_me')

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)

                if not remember_me:  
                    request.session.set_expiry(0)  # Sesión expira al cerrar navegador
                else:
                    request.session.set_expiry(1209600)  # 2 semanas de sesión activa

                messages.success(request, 'Ha Iniciado Sesión Con Éxito')
                return redirect('home')
            else:
                messages.error(request, 'Credenciales de acceso invalidos')
                return redirect('login')
        else:
            form = LoginForm()
            context = {
                'form' : form
            }    
            return render(request, 'usuarios/login.html', context)
        
@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('login')

def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Usuario.objects.filter(email=email).exists():
            user = Usuario.objects.get(email__exact=email)
            
            # Reset password email
            current_site = get_current_site(request)
            mail_subject = 'Restablecer su contraseña'
            message = render_to_string('usuarios/reset-password-email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Se ha enviado un correo electrónico de restablecimiento de contraseña a su dirección de correo electrónico.')
            return redirect('login')
        else:
            messages.error(request, '¡La cuenta no existe!')
            return redirect('forgotPassword')
    else:           
        return render(request, 'usuarios/reset-password.html')   