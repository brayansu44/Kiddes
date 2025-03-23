# Generated by Django 5.1.7 on 2025-03-22 22:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FacturaCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_factura', models.CharField(max_length=20)),
                ('proveedor', models.CharField(max_length=50)),
                ('fecha_emision', models.DateField(auto_now_add=True)),
                ('fecha_vencimiento', models.DateField()),
                ('monto_total', models.FloatField()),
                ('saldo_pendiente', models.FloatField()),
            ],
            options={
                'verbose_name': 'Factura de Compra',
                'verbose_name_plural': 'Facturas de Compra',
            },
        ),
        migrations.CreateModel(
            name='FacturaVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_factura', models.CharField(max_length=20)),
                ('fecha_emision', models.DateField(auto_now_add=True)),
                ('fecha_vencimiento', models.DateField()),
                ('monto_total', models.FloatField()),
                ('saldo_pendiente', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cuentas.cliente')),
            ],
            options={
                'verbose_name': 'Factura de Venta',
                'verbose_name_plural': 'Facturas de Venta',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_pagado', models.FloatField()),
                ('fecha_pago', models.DateField(auto_now_add=True)),
                ('metodo_pago', models.CharField(choices=[('Efectivo', 'Efectivo'), ('Transferencia', 'Transferencia'), ('Tarjeta', 'Tarjeta de Crédito/Débito')], max_length=50)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cuentas.facturacompra')),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Pagos',
            },
        ),
        migrations.CreateModel(
            name='PagoRecibido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto_pagado', models.FloatField()),
                ('fecha_pago', models.DateField(auto_now_add=True)),
                ('metodo_pago', models.CharField(choices=[('Efectivo', 'Efectivo'), ('Transferencia', 'Transferencia'), ('Tarjeta', 'Tarjeta de Crédito/Débito')], max_length=50)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cuentas.facturaventa')),
            ],
            options={
                'verbose_name': 'Pago Recibido',
                'verbose_name_plural': 'Pagos Recibidos',
            },
        ),
    ]
