# Generated by Django 5.1.7 on 2025-04-14 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodega', '0014_alter_salidaproducto_local'),
        ('locales', '0002_local_encargado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salidaproducto',
            name='local',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locales.inventariolocal'),
        ),
    ]
