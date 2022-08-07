import jwt
from datetime import timedelta

from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone
from django.urls import reverse_lazy

from apps.core.models import Audit
from apps.core.validators import telefono_regex
from apps.geolocalizaciones.comportamientos import Geolocalizable
from apps.usuarios.models.usuarios import Usuario


# Create your models here.
class Empresa(Geolocalizable, Audit):
    administrador = models.ForeignKey(
        'usuarios.Usuario',
        null=True,
        blank=True,
        verbose_name='Administrador',
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

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nombre_comercial

    @property
    def token_invitacion(self):
        fecha_expiracion = timezone.now() + timedelta(days=3)
        payload = {
            'administrador': self.administrador.email,
            'exp': int(fecha_expiracion.timestamp()),
            'tipo': 'invitacion_administrador'
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return token

@receiver(post_save, sender=Empresa)
def invitar_administrador(sender, **kwargs):
    # write you functionality
    instance = kwargs['instance']
    update_fields = kwargs['update_fields']

    if update_fields:
        asunto = 'Invitación de administración'
        ruta = reverse_lazy('usuarios:administradores.validar_invitacion', args=[instance.token_invitacion])
        context = {
            'nombre': f'{instance.administrador.first_name} {instance.administrador.last_name}',
            'nombre_empresa': instance.nombre_comercial,
            'enlace': f'{settings.DOMAIN_NAME}{ruta}'
        }
        html_message = render_to_string(
            'core/startbootstrap/email.html',
            context=context
        )
        mensage = strip_tags(html_message)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [f'{instance.administrador.email}']
        send_mail(asunto, mensage, email_from, recipient_list, html_message=html_message)
    else:
        Usuario.objects.filter(pk=instance.administrador.pk).update(empresa=instance)
