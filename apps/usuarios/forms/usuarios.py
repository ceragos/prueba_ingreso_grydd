from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crum import get_current_user
from django import forms
from django.conf import settings
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.html import strip_tags
from geolocation_fields.forms import fields

from apps.gestiones.models.empresas import Empresa
from apps.usuarios.models import Usuario


class UsuarioForm(forms.ModelForm):
    geolocalizacion = fields.PointField(label='Geolocalización')

    class Meta:
        model = Usuario
        fields = (
            'last_name',
            'first_name',
            'empresa',
            'direccion',
            'telefono',
            'email',
            'pais',
            'estado',
            'ciudad',
            'geolocalizacion',
            'pais_estado_ciudad'
        )

    def __init__(self, empresa=None, point_map_center=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-empresaForm'
        self.helper.form_class = 'container'
        self.helper.form_method = 'post'
        # self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Enviar', css_class='btn btn-primary mt-4'))

        self.fields['last_name'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['first_name'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['empresa'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['direccion'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['telefono'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['pais'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['estado'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['ciudad'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['pais_estado_ciudad'].widget.attrs['class'] = 'form-control form-control-solid'

        if empresa:
            self.initial['empresa'] = empresa
            self.fields['empresa'].widget = forms.HiddenInput()
        if point_map_center:
            self.initial['geolocalizacion'] = point_map_center


class UsuarioAdministradorForm(UsuarioForm):

    def save(self, commit=True):
        instance = super(UsuarioAdministradorForm, self).save(commit=False)
        instance.is_staff = True
        if commit:
            instance.save()
        return instance


class EstablecerContrasenaFrom(forms.Form):
    email = forms.ModelChoiceField(Usuario.objects.all())
    password = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password_confirmation = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text="Ingrese la misma contraseña que antes, para verificación.",
    )
    
    def __init__(self, email=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email
        if self.email:
            self.initial['email'] = self.email
            self.fields['email'].widget = forms.HiddenInput()
        self.helper = FormHelper()
        self.helper.form_id = 'id-usuarioForm'
        self.helper.form_class = 'container'
        self.helper.form_method = 'post'
        # self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Enviar', css_class='btn btn-primary mt-4'))

        self.fields['password'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['password_confirmation'].widget.attrs['class'] = 'form-control form-control-solid'

    def clean_password_confirmation(self):
        password = self.cleaned_data.get("password")
        password_confirmation = self.cleaned_data.get("password_confirmation")
        if password and password_confirmation and password != password_confirmation:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password_confirmation

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password_confirmation')
        usuario = Usuario.objects.get(email=self.cleaned_data["email"])
        if password:
            try:
                password_validation.validate_password(password, usuario)
            except ValidationError as error:
                self.add_error('password_confirmation', error)

    def save(self):
        usuario = Usuario.objects.filter(email=self.cleaned_data["email"]).first()
        password = self.cleaned_data["password"]
        usuario.set_password(password)
        usuario.save()
        return usuario


class InvitarEmpleadoFrom(forms.Form):
    email = forms.EmailField(label='Correo electrónico')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-usuarioForm'
        self.helper.form_class = 'container'
        self.helper.form_method = 'post'
        # self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Enviar', css_class='btn btn-primary mt-4'))

        self.fields['email'].widget.attrs['class'] = 'form-control form-control-solid'

    def is_valid(self):
        is_valid = super().is_valid()
        if is_valid:
            empresa= Empresa.objects.filter(pk=get_current_user().empresa.pk).first()
            asunto = 'Invitación de empleado'
            ruta = reverse_lazy('usuarios:empleados.registrar', args=[empresa.pk])
            context = {
                'nombre_empresa': empresa.nombre_comercial,
                'enlace': f'{settings.DOMAIN_NAME}{ruta}'
            }
            html_message = render_to_string(
                'usuarios/empleados/email.html',
                context=context
            )
            mensage = strip_tags(html_message)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [f'{self.cleaned_data["email"]}']
            send_mail(asunto, mensage, email_from, recipient_list, html_message=html_message)
        return is_valid
