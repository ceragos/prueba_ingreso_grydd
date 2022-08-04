from django.db import models
from geolocation_fields.models import fields

from apps.core.models import Audit
from apps.gestiones.models import Empresa

# Create your models here.
class PuntoAcceso(Audit):
    nombre = models.CharField(
        max_length=80,
        verbose_name='Nombre'
    )
    direccion = models.CharField(
        max_length=80,
        verbose_name='Dirección'
    )
    email = models.EmailField(
        'Correo electrónico',
        unique=True,
        error_messages={
            'unique': 'Ya existe un usuario con ese correo electrónico.'
        }
    )
    empresa = models.ForeignKey(
        Empresa,
        verbose_name='Empresa',
        related_name='sedes_empresa',
        on_delete=models.PROTECT
    )
    geolocalizacion = fields.PointField(
        verbose_name='geolocalización'
    )
    horarios_acceso = models.ManyToManyField(
        'gestiones.FranjaHoraria',
        blank=True,
        verbose_name='Horarios de acceso',
        related_name='sedes_franja'
    )

    class Meta:
        verbose_name = 'Punto de acceso'
        verbose_name_plural = 'Puntos de acceso'

    def __str__(self):
        return f'{self.empresa} - {self.nombre}'
