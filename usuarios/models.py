from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("El usuario debe tener una dirección de correo electrónico.")

        if not username:
            raise ValueError("El usuario debe tener un nombre de usuario")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):   
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    username                = models.CharField(max_length=50, unique=True)
    email                   = models.EmailField(max_length=100, unique=True)
    cargo                     = models.ForeignKey("Cargo", on_delete=models.SET_NULL, null=True, blank=True)

    # required
    date_joined             = models.DateTimeField(auto_now_add=True)
    last_login              = models.DateTimeField(auto_now_add=True)
    is_staff                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)
    #is_superadmin           = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

class PerfilUsuario(models.Model):
    usuario     = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nombre      = models.CharField(max_length=50)
    apellido    = models.CharField(max_length=50)
    documento   = models.IntegerField(unique=True)
    telefono    = models.IntegerField(unique=True)

    def __str__(self):
        return self.nombre
    
    def full_name(self):
        return f'{self.nombre} {self.apellido}'
    
class Cargo(models.Model):
    nombre  = models.CharField(max_length=50, unique=True)
    area    = models.ForeignKey("Area", on_delete=models.SET_NULL, null=True, blank=True)  

    def __str__(self):
        return self.nombre

class Area(models.Model):
    nombre      = models.CharField(max_length=100, unique=True, null=False, blank=False)
    descripcion = models.CharField(max_length=100)
    empresa     = models.ForeignKey("Empresa", on_delete=models.SET_NULL, null=True, blank=True)

    def _str_(self):
        return self.nombre

class Empresa(models.Model):
    nombre                  = models.CharField(max_length=100, unique=True)
    razon_social            = models.CharField(max_length=100)
    nit                     = models.IntegerField(unique=True)
    telefono                = models.IntegerField(unique=True)
    correo                  = models.EmailField(max_length=100, unique=True)
    fecha_inicio_actividad  = models.DateField()
    usuario                 = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)

    def _str_(self):
        return self.nombre       