# Generated by Django 5.1 on 2024-10-18 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesor', '0002_rename_descripción_profesor_descripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesor',
            old_name='descripcion',
            new_name='nombre',
        ),
    ]
