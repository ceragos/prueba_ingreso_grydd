from django.db import models

from apps.core.models import Audit, ParametroBaseModel

# Create your models here.
class Pais(ParametroBaseModel, Audit):
    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'


class Estado(ParametroBaseModel, Audit):
    pais = models.ForeignKey(
        Pais,
        verbose_name='País',
        on_delete=models.PROTECT,
        related_name='estados_pais'
    )

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'


class Ciudad(ParametroBaseModel, Audit):
    estado = models.ForeignKey(
        Estado,
        verbose_name='Estado',
        on_delete=models.PROTECT,
        related_name='ciudades_estado'
    )

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
