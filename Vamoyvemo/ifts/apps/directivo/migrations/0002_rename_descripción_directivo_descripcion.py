# Generated by Django 5.1 on 2024-09-05 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directivo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='directivo',
            old_name='descripción',
            new_name='descripcion',
        ),
    ]
