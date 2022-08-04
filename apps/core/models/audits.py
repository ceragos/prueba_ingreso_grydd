from datetime import datetime

from crum import get_current_user, get_current_request
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.core.models import BaseModel


class Audit(BaseModel):
    """
    Esta clase genera automáticamente un registro de los cambios que se realizan la información de una instancia
    de las clases que hereden de ella.
    """
    is_active = models.BooleanField(default=True, verbose_name=_('activo'))
    removed = models.BooleanField(default=False, verbose_name=_('eliminado'))
    # Auditoria de creación
    created_by = models.ForeignKey('usuarios.Usuario', null=True, blank=True, verbose_name='creado por',
                                   related_name='%(class)s_created_by', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name=_('fecha de creación'))
    creation_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name=_('ip de creación'))
    # Auditoria de modificación
    modified_by = models.ForeignKey('usuarios.Usuario', null=True, blank=True, verbose_name=_('modificado por'),
                                    related_name='%(class)s_modified_by', on_delete=models.CASCADE)
    modification_date = models.DateTimeField(null=True, blank=True, verbose_name=_('fecha de modificación'))
    modification_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name=_('ip de modificación'))
    # Auditoria de borrado
    removed_by = models.ForeignKey('usuarios.Usuario', null=True, blank=True, verbose_name='eliminado por',
                                   related_name='%(class)s_removed_by', on_delete=models.CASCADE)
    elimination_date = models.DateTimeField(null=True, blank=True, verbose_name=_('fecha de eliminación'))
    elimination_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name=_('ip de eliminación'))

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):

        """
        Si el estado de la instancia es de creación se genera un registro de
        quien, cuando y desde donde se crea la instancia.
        De lo contrario el estado corresponde a una modificación, por lo cual
        se genera un registro de quien, cuando y desde donde se modifica la instancia.
        """
        if self._state.adding:
            self.created_by = get_current_user()
            self.creation_ip = get_current_request().META['REMOTE_ADDR']
        else:
            self.modified_by = get_current_user()
            self.modification_date = datetime.now()
            self.modification_ip = get_current_request().META['REMOTE_ADDR']

        super(Audit, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.removed_by = get_current_user()
        self.elimination_date = datetime.now()
        self.elimination_ip = get_current_request().META['REMOTE_ADDR']
        self.removed = True
        self.save()
