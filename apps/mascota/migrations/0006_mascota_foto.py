# Generated by Django 2.0.9 on 2018-12-30 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0005_remove_mascota_deportista'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
