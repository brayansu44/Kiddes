# Generated by Django 5.1.7 on 2025-03-22 22:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proveedores', '0002_initial'),
        ('telas', '0001_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cortetela',
            name='responsable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.perfilusuario'),
        ),
        migrations.AddField(
            model_name='ordenproduccion',
            name='cortador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordenes_produccion', to='usuarios.perfilusuario'),
        ),
        migrations.AddField(
            model_name='cortetela',
            name='orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cortes', to='telas.ordenproduccion'),
        ),
        migrations.AddField(
            model_name='cortetela',
            name='rollo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telas.rollotela'),
        ),
        migrations.AddField(
            model_name='tallacorte',
            name='corte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tallas_cortes', to='telas.cortetela'),
        ),
        migrations.AddField(
            model_name='componentecorte',
            name='talla_corte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='componentes_tela', to='telas.tallacorte'),
        ),
        migrations.AddField(
            model_name='tela',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.proveedor'),
        ),
        migrations.AddField(
            model_name='rollotela',
            name='tela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telas.tela'),
        ),
    ]
