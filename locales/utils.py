from django.utils.timezone import now
from datetime import date
from .models import InventarioLocal, InventarioSemanal, VentaSemanal

def registrar_inventario_semanal():
    """ Registra el inventario de cada local semanalmente cada lunes. """
    hoy = date.today()
    semana_actual = hoy.isocalendar()[1]
    anio_actual = hoy.year

    locales = InventarioLocal.objects.values_list('local', flat=True).distinct()

    for local_id in locales:
        variantes = InventarioLocal.objects.filter(local_id=local_id)

        for inv in variantes:
            entradas = inv.entradas
            salidas = inv.salidas
            stock_final = inv.stock_actual

            # Guardar en InventarioSemanal
            InventarioSemanal.objects.update_or_create(
                local_id=local_id,
                variante=inv.variante,
                semana=semana_actual,
                anio=anio_actual,
                defaults={
                    'entradas': entradas,
                    'salidas': salidas,
                    'stock_final': stock_final
                }
            )

            # Guardar en VentaSemanal
            VentaSemanal.objects.update_or_create(
                local_id=local_id,
                variante=inv.variante,
                semana=semana_actual,
                anio=anio_actual,
                defaults={
                    'cantidad_vendida': salidas
                }
            )
