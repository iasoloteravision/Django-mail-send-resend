# Generated by Django 4.2.3 on 2024-01-05 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_contenido_mostrar_en_pagina_dinamica'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenido',
            name='destinatario',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]