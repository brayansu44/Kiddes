# Generated by Django 5.1.7 on 2025-03-29 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodega', '0005_confirmacionrecepcion_observaciones_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insumo',
            name='cantidad',
        ),
        migrations.AddField(
            model_name='tipoinsumo',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='unidadmedida',
            name='abrev',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
