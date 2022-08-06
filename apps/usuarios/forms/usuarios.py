import email
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

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


class UsuarioAdministradorForm(UsuarioForm):

    def __init__(self, empresa=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.empresa = empresa
        if self.empresa:
            self.initial['empresa'] = self.empresa
            self.fields['empresa'].widget = forms.HiddenInput()

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
