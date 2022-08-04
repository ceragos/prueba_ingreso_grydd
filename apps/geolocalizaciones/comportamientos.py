from pyexpat import model
from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from apps.geolocalizaciones.models import Pais, Estado, Ciudad

class Geolocalizable(models.Model):
    
    pais = models.ForeignKey(
        Pais,
        null=True,
        verbose_name='País',
        related_name='%(class)ss_pais',
        on_delete=models.PROTECT
    )
    estado = ChainedForeignKey(
        Estado,
        null=True,
        chained_field="pais",
        chained_model_field="pais",
        show_all=False,
        auto_choose=True,
        sort=True,
        related_name='%(class)ss_estado'
    )
    ciudad = ChainedForeignKey(
        Ciudad,
        null=True,
        chained_field="estado",
        chained_model_field="estado",
        show_all=False,
        auto_choose=True,
        sort=True,
        related_name='%(class)ss_ciudad'
    )

    class Meta:
        abstract = True