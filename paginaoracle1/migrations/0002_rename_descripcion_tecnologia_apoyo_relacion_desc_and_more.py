# Generated by Django 5.2.4 on 2025-07-14 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paginaoracle1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tecnologia_apoyo',
            old_name='descripcion',
            new_name='relacion_desc',
        ),
        migrations.RenameField(
            model_name='tecnologia_apoyo',
            old_name='nombre',
            new_name='tecnologia_progra',
        ),
    ]
