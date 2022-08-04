from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

from apps.core.validators import telefono_regex


class Usuario(AbstractUser):
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
    telefono = models.CharField(
        max_length=17,
        validators=[telefono_regex]
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
