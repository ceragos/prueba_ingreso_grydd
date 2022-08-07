from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crum import get_current_user
from django import forms

from apps.gestiones.models import PuntoAcceso

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

        if not get_current_user().is_superuser:
            self.initial['empresa'] = get_current_user().empresa
            self.fields['empresa'].widget = forms.HiddenInput()
