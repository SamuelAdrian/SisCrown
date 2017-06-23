# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-22 23:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
        ('cliente', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Oportunidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('negociacion', models.TextField()),
                ('modelo_actual', models.CharField(blank=True, max_length=50)),
                ('modelo_interes', models.CharField(blank=True, max_length=50)),
                ('tipo_venta', models.CharField(choices=[('CONTADO', 'Contado'), ('CREDITO', 'Credito'), ('AUTOFACIL', 'AutoFacil'), ('OTRO', 'Otro')], default='OTRO', max_length=30)),
                ('estado', models.CharField(choices=[('VIGENTE', 'Vigente'), ('EXITOSA', 'Venta Exitosa'), ('CAIDA', 'Venta Caida'), ('SUSPENDIDA', 'Suspendida Temporalmente')], default='VIGENTE', max_length=30)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('agencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Agencia')),
                ('dni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
                ('vendedor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_vehiculos', models.CharField(choices=[('CAMION', 'Camion'), ('MOTO', 'Moto'), ('VEHICULOLIVIANO', 'Vehiculo Liviano')], default='VEHICULOLIVIANO', max_length=30)),
                ('referencia', models.CharField(choices=[('PERSONAL', 'Personal'), ('REDES', 'Redes'), ('RADIO', 'Radio'), ('VOLANTES', 'Volantes'), ('SHOWROOM', 'Show Room'), ('OTRO', 'Otro')], max_length=30)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('agencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Agencia')),
                ('dni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
                ('vendedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
