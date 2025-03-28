# Generated by Django 5.1.7 on 2025-03-22 22:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Producto', '0001_initial'),
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiasFuncionamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.IntegerField(choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miércoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sábado'), (7, 'Domingo')], unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=255)),
                ('Horario_habil', models.ManyToManyField(related_name='locales', to='locales.diasfuncionamiento')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Empresa_relacionada', to='empresas.empresa')),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locales',
            },
        ),
        migrations.CreateModel(
            name='InventarioSemanal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semana', models.DateField()),
                ('anio', models.IntegerField(default=2025)),
                ('entradas', models.PositiveIntegerField(default=0)),
                ('salidas', models.PositiveIntegerField(default=0)),
                ('stock_final', models.PositiveIntegerField(default=0)),
                ('variante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Producto.productovariante')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locales.local')),
            ],
            options={
                'unique_together': {('local', 'variante', 'semana', 'anio')},
            },
        ),
        migrations.CreateModel(
            name='InventarioLocal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entradas', models.PositiveIntegerField(default=0)),
                ('salidas', models.PositiveIntegerField(default=0)),
                ('stock_actual', models.PositiveIntegerField(default=0)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('variante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_locales', to='Producto.productovariante')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventario', to='locales.local')),
            ],
            options={
                'verbose_name': 'Inventario Local',
                'verbose_name_plural': 'Inventario Local',
                'unique_together': {('local', 'variante')},
            },
        ),
        migrations.CreateModel(
            name='VentaSemanal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semana', models.DateField()),
                ('anio', models.IntegerField(default=2025)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('cantidad_vendida', models.PositiveIntegerField(default=0)),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locales.local')),
                ('variante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Producto.productovariante')),
            ],
            options={
                'unique_together': {('local', 'variante', 'semana', 'anio')},
            },
        ),
    ]
