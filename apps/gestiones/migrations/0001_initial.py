# Generated by Django 3.1.5 on 2022-08-03 23:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geolocalizaciones', '0001_initial'),
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
                ('administrador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='empresas_administradas', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('ciudad', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='estado', chained_model_field='estado', on_delete=django.db.models.deletion.CASCADE, to='geolocalizaciones.ciudad')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empresa_created_by', to=settings.AUTH_USER_MODEL, verbose_name='creado por')),
                ('estado', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='pais', chained_model_field='pais', on_delete=django.db.models.deletion.CASCADE, to='geolocalizaciones.estado')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empresa_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='modificado por')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='empresas_pais', to='geolocalizaciones.pais', verbose_name='País')),
                ('removed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empresa_removed_by', to=settings.AUTH_USER_MODEL, verbose_name='eliminado por')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
    ]