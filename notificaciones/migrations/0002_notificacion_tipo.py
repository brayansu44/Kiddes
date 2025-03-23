# Generated by Django 5.1.7 on 2025-03-23 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notificaciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacion',
            name='tipo',
            field=models.CharField(choices=[('salida', 'Salida de Producto'), ('confirmacion', 'Confirmación de Recepción'), ('otro', 'Otro')], default='otro', max_length=20),
        ),
    ]
