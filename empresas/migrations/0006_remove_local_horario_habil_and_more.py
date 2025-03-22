# Generated by Django 5.1.7 on 2025-03-20 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0005_alter_local_empresa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='local',
            name='Horario_habil',
        ),
        migrations.AlterUniqueTogether(
            name='inventariolocal',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='inventariolocal',
            name='local',
        ),
        migrations.RemoveField(
            model_name='inventariolocal',
            name='variante',
        ),
        migrations.RemoveField(
            model_name='local',
            name='empresa',
        ),
        migrations.DeleteModel(
            name='DiasFuncionamiento',
        ),
    ]
