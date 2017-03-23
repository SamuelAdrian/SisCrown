# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0008_cpu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesorio',
            fields=[
                ('serie', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(choices=[('RATON', 'Raton'), ('TECLADO', 'Teclado'), ('HDDEXT', 'Disco Duro Externo'), ('IMPRESORA', 'Pen'), ('MUSB', 'Memoria USB')], max_length=20)),
                ('marca', models.CharField(blank=True, max_length=30)),
                ('modelo', models.CharField(blank=True, max_length=30)),
                ('caracteristica', models.CharField(blank=True, max_length=50)),
                ('observacion', models.TextField(blank=True)),
                ('departamento_adquisicion', models.CharField(blank=True, choices=[('LAPAZ', 'La Paz'), ('SANTACRUZ', 'Santa Cruz'), ('COCHABAMBA', 'Cochabamba'), ('ORURO', 'Oruro'), ('POTOSI', 'Potosi'), ('TARIJA', 'Tarija'), ('SUCRE', 'Sucre'), ('BENI', 'Beni'), ('PANDO', 'Pando')], max_length=20)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
