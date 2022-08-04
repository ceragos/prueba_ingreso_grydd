from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from apps.usuarios.models import Usuario

class UsuarioForm(forms.ModelForm):
    
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
            'ciudad'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-empresaForm'
        self.helper.form_class = 'container'
        self.helper.form_method = 'post'
        # self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-primary'))

        self.fields['last_name'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['first_name'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['empresa'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['direccion'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['telefono'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['pais'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['estado'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['ciudad'].widget.attrs['class'] = 'form-control form-control-solid'


class UsuarioAdministradorForm(UsuarioForm):

    def save(self, commit=True):
        instance = super(UsuarioAdministradorForm, self).save(commit=False)
        instance.is_staff = True
        if commit:
            instance.save()
        return instance
