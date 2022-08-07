from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from phonenumber_field.modelfields import PhoneNumberField

from apps.core.validators import telefono_regex
from apps.geolocalizaciones.comportamientos import Geolocalizable


class Usuario(AbstractUser, Geolocalizable):
    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': 'Ya existe un usuario con ese email.'
        }
    )
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        null=True,
        blank=True,
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    telefono = PhoneNumberField()
    direccion = models.CharField(
        max_length=80,
        verbose_name='Dirección'
    )
    empresa = models.ForeignKey(
        'gestiones.Empresa',
        null=True,
        blank=False,
        verbose_name='Empresa',
        related_name='empleados_empresa',
        on_delete=models.PROTECT
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
