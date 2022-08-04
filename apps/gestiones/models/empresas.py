from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from apps.core.models import Audit
from apps.core.validators import telefono_regex
from apps.geolocalizaciones.models import Pais, Estado, Ciudad

# Create your models here.
class Empresa(Audit):
    administrador = models.ForeignKey(
        'usuarios.Usuario',
        null=True,
        blank=True,
        verbose_name='Usuario',
        related_name='empresas_administradas',
        on_delete=models.PROTECT
    )
    nit = models.CharField(
        max_length=11,
        verbose_name='NIT',
        unique=True
    )
    nombre = models.CharField(
        max_length=80,
        verbose_name='Nombre'
    )
    nombre_comercial = models.CharField(
        max_length=80,
        verbose_name='Nombre comercial'
    )
    direccion = models.CharField(
        max_length=80,
        verbose_name='Dirección'
    )
    telefono = models.CharField(
        max_length=17,
        validators=[telefono_regex]
    )
    email = models.EmailField(
        'Correo electrónico',
        unique=True,
        error_messages={
            'unique': 'Ya existe un usuario con ese correo electrónico.'
        }
    )
    sitio_web = models.URLField(
        max_length=200,
        verbose_name='Sitio web'
    )
    pais = models.ForeignKey(
        Pais,
        verbose_name='País',
        related_name='empresas_pais',
        on_delete=models.PROTECT
    )
    estado = ChainedForeignKey(
        Estado,
        chained_field="pais",
        chained_model_field="pais",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    ciudad = ChainedForeignKey(
        Ciudad,
        chained_field="estado",
        chained_model_field="estado",
        show_all=False,
        auto_choose=True,
        sort=True
    )

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nombre_comercial
