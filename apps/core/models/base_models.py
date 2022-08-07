from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):

        # self.format_characters()

        super(BaseModel, self).save(*args, **kwargs)

    def format_characters(self):
        # Obtiene todos los campos de tipo charfield
        char_fields = [field.name for field in self._meta.fields if
                       isinstance(field, models.CharField) and not getattr(field, 'choices')]
        for field in char_fields:
            valor = getattr(self, field, False)
            if valor:
                # Elimina los espacios en blanco que no son necesarios
                valor = " ".join(valor.split())
                # Cambia los caracteres a mayusculas
                setattr(self, field, valor.title())


class ParametroBaseModel(BaseModel):

    nombre = models.CharField(
        null=False,
        blank=False,
        verbose_name=_('nombre'),
        max_length=120
    )
    abvr = models.CharField(
        null=True,
        blank=True,
        verbose_name=_('abreviatura'),
        max_length=30
    )
    descripcion = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('descripción'),
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre
