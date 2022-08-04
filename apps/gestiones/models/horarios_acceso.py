from django.db import models

from apps.core.models import Audit

# Create your models here.
class FranjaHoraria(Audit):
    punto_acceso = models.ForeignKey(
        'gestiones.PuntoAcceso',
        verbose_name='Punto de acceso',
        related_name='horarios_sede',
        on_delete=models.PROTECT
    )
    hora_inicio = models.TimeField(
        verbose_name='Hora de inicio'
    )
    hora_finalizacion = models.TimeField(
        verbose_name='Hora de finalización'
    )
    empleado = models.ForeignKey(
        'usuarios.Usuario',
        verbose_name='Usuario',
        related_name='horarios_empleado',
        on_delete=models.PROTECT
    )