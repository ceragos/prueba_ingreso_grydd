# Generated by Django 3.1.5 on 2022-08-04 00:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='activo')),
                ('removed', models.BooleanField(default=False, verbose_name='eliminado')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('creation_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de creación')),
                ('modification_date', models.DateTimeField(blank=True, null=True, verbose_name='fecha de modificación')),
                ('modification_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de modificación')),
                ('elimination_date', models.DateTimeField(blank=True, null=True, verbose_name='fecha de eliminación')),
                ('elimination_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip de eliminación')),
                ('nit', models.CharField(max_length=11, unique=True, verbose_name='NIT')),
                ('nombre', models.CharField(max_length=80, verbose_name='Nombre')),
                ('nombre_comercial', models.CharField(max_length=80, verbose_name='Nombre comercial')),
                ('direccion', models.CharField(max_length=80, verbose_name='Dirección')),
                ('telefono', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='El número de teléfono debe ingresarse en el formato: +999999999999. Se permiten hasta 15 dígitos.', regex='\\+?2?\\d{9,15}$')])),
                ('email', models.EmailField(error_messages={'unique': 'Ya existe un usuario con ese correo electrónico.'}, max_length=254, unique=True, verbose_name='Correo electrónico')),
                ('sitio_web', models.URLField(verbose_name='Sitio web')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
    ]
