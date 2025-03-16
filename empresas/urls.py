from django.urls import path
from . import views

urlpatterns = [
    path('', views.empresas, name='empresas'),
    path('locales/', views.locales, name='locales'),
    path('inventario-local/<int:local_id>/', views.inventario_local, name='inventario_local'),
    path('resumen-inventario-producto/<int:producto_id>/', views.resumen_inventario_producto, name='resumen_inventario_producto'),
]    