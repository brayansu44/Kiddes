# Generated by Django 5.1.6 on 2025-03-15 18:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0003_alter_inventariolocal_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventariolocal',
            old_name='cantidad_disponible',
            new_name='entradas',
        ),
        migrations.RenameField(
            model_name='inventariolocal',
            old_name='stock_minimo',
            new_name='salidas',
        ),
        migrations.RemoveField(
            model_name='inventariolocal',
            name='fecha_actualizada',
        ),
        migrations.AddField(
            model_name='inventariolocal',
            name='fecha',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventariolocal',
            name='stock_actual',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
