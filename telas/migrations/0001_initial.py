# Generated by Django 5.1.6 on 2025-03-09 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComponentesTela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_pieza', models.CharField(choices=[('Delantero', 'Delantero'), ('Posterior', 'Posterior'), ('Mangas', 'Mangas'), ('Cuellos', 'Cuellos'), ('Bolsillos', 'Bolsillos')], default='Delantero', max_length=50)),
                ('cantidad', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CorteTela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('largo_utilizado', models.DecimalField(decimal_places=2, max_digits=6)),
                ('capas_cortadas', models.PositiveIntegerField()),
                ('colas', models.DecimalField(decimal_places=2, max_digits=6)),
                ('faltante_tela', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rendimiento_rollo', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fecha_corte', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrdenProduccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('referencia', models.CharField(max_length=100, unique=True)),
                ('total_unidades', models.PositiveIntegerField()),
                ('observaciones', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Orden Produccion',
                'verbose_name_plural': 'Orden Produccion',
            },
        ),
        migrations.CreateModel(
            name='RolloTela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('largo_inicial', models.DecimalField(decimal_places=2, max_digits=6)),
                ('largo_restante', models.DecimalField(decimal_places=2, max_digits=6)),
                ('estado', models.CharField(choices=[('Completo', 'Completo'), ('Incompleto', 'Incompleto')], default='Completo', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TallaCorte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talla', models.CharField(choices=[('S', 'Pequeño'), ('M', 'Mediano'), ('L', 'Grande'), ('XL', 'Extra Grande')], default='S', max_length=2)),
                ('cantidad', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('color', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('proveedor', models.CharField(max_length=100)),
                ('ancho', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
