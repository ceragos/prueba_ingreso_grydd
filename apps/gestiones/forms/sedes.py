import logging

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crum import get_current_user, get_current_request
from django import forms
from ipware import get_client_ip

from apps.gestiones.models import PuntoAcceso, FranjaHoraria

logger = logging.getLogger('GESTIONES')


class PuntoAccesoForm(forms.ModelForm):
    
    class Meta:
        model = PuntoAcceso
        fields = (
            'nombre',
            'direccion',
            'email',
            'empresa',
            'geolocalizacion',
            'horarios_acceso',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-empresaForm'
        self.helper.form_class = 'container'
        self.helper.form_method = 'post'
        # self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Enviar', css_class='btn btn-primary mt-4'))

        self.fields['nombre'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['direccion'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['empresa'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['geolocalizacion'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['horarios_acceso'].widget.attrs['class'] = 'form-control form-control-solid'

        current_user = get_current_user()
        self.fields['horarios_acceso'].queryset = self.fields['horarios_acceso'].queryset.filter(punto_acceso__empresa=current_user.empresa)
        if not current_user.is_superuser:
            self.initial['empresa'] = current_user.empresa
            self.fields['empresa'].widget = forms.HiddenInput()
        self.get_geolocalizacion()

    def get_geolocalizacion(self):
        request =get_current_request()
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        logger.info('request', ip, is_routable)
        ip, is_routable = get_client_ip(request)
        logger.info('ipware', ip, is_routable)
        f'http://ip-api.com/json/{ip}'
