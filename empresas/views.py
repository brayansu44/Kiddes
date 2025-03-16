from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Max, Count

from .models import Empresa, Local, InventarioLocal
from Producto.models import Producto, ProductoVariante

@login_required(login_url = 'login')
def empresas(request):
    empresas        = Empresa.objects.annotate(locales_count=Count('Empresa_relacionada'), 
                                               usuarios_count=Count('Empresa_usuario__perfil'))
    context = {
        'empresas': empresas,
    }

    return render(request, 'empresas/empresas.html', context)

@login_required(login_url = 'login')
def locales(request):
    locales = Local.objects.all()
    return render(request, 'empresas/locales.html', {'locales': locales})

@login_required(login_url = 'login')
def inventario_local(request, local_id):
    local = get_object_or_404(Local, id=local_id)
    inventario = InventarioLocal.objects.filter(local=local).select_related('variante__producto')

    context = {
        'local': local,
        'inventario': inventario,
    }

    return render(request, 'empresas/inventario-local.html', context)

@login_required(login_url = 'login')
def resumen_inventario_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    inventario = InventarioLocal.objects.filter(variante__producto=producto) \
        .values('variante__talla__nombre') \
        .annotate(stock_total=Sum('stock_actual'), salidas_total=Sum('salidas')) \
        .order_by('variante__talla__nombre')
    fecha_actualizacion = InventarioLocal.objects.filter(variante__producto=producto).aggregate(ultima_fecha=Max('fecha'))['ultima_fecha']
    total_stock = sum(item['stock_total'] for item in inventario)
    total_salidas = sum(item['salidas_total'] for item in inventario)

    context = {
        'producto': producto,
        'inventario': inventario,
        'fecha': fecha_actualizacion,
        'total_stock': total_stock,
        'total_salidas': total_salidas
    }
    return render(request, 'empresas/resumen-inventario.html', context)