import logging

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crum import get_current_user
from django import forms

from apps.gestiones.models import PuntoAcceso

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
            'is_active'
        )

    def __init__(self, point_map_center=None, *args, **kwargs):
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

        if point_map_center:
            self.initial['geolocalizacion'] = point_map_center

        current_user = get_current_user()
        self.fields['horarios_acceso'].queryset = self.fields['horarios_acceso'].queryset.filter(punto_acceso__empresa=current_user.empresa)
        
        if not current_user.is_superuser:
            self.initial['empresa'] = current_user.empresa
            self.fields['empresa'].widget = forms.HiddenInput()
