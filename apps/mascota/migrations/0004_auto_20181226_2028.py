# Generated by Django 2.0.9 on 2018-12-27 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0003_auto_20181226_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascota',
            old_name='perros',
            new_name='vacuna',
        ),
    ]
