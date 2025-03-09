from django.urls import path
from . import views

urlpatterns = [
    path('proveedores/', views.proveedores, name='proveedores'),
]    