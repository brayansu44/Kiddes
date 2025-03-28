# Generated by Django 5.1.7 on 2025-03-29 04:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodega', '0006_remove_insumo_cantidad_tipoinsumo_activo_and_more'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entregacorte',
            name='cantidad_lavado',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='salidaproducto',
            name='es_lavado',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='EntradaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('cantidad', models.PositiveIntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entradas', to='bodega.stock')),
                ('user_responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.perfilusuario')),
            ],
        ),
    ]
