# Generated by Django 5.1.7 on 2025-03-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodega', '0010_alter_entradaproducto_cantidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usoinsumo',
            name='uso_destino',
            field=models.CharField(choices=[('Costura', 'Costura'), ('Otros', 'Otros')], default='Lavado', max_length=50),
        ),
    ]
