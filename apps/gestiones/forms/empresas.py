from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from apps.gestiones.models import Empresa

class EmpresaForm(forms.ModelForm):
    
    class Meta:
        model = Empresa
        fields = (
            'nit',
            'nombre',
            'nombre_comercial',
            'direccion',
            'telefono',
            'email',
            'sitio_web',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-empresaForm'
        self.helper.form_class = 'container'
        self.helper.form_method = 'post'
        # self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-primary'))

        self.fields['nit'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['nombre'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['nombre_comercial'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['direccion'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['telefono'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['sitio_web'].widget.attrs['class'] = 'form-control form-control-solid'
