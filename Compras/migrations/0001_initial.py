# Generated by Django 5.1.7 on 2025-03-22 22:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cuentas', '0001_initial'),
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gastos_Operativos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Tipo_gasto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('EmpresaID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.empresa')),
                ('Factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cuentas.facturacompra')),
            ],
        ),
    ]
