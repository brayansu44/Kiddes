# Generated by Django 5.1.7 on 2025-03-20 21:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodega', '0003_initial'),
        ('locales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salidas_producto',
            name='LocalID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locales.inventariolocal'),
        ),
    ]
