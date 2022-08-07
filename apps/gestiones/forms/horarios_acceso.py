from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crum import get_current_user
from django import forms

from apps.gestiones.models import FranjaHoraria

class CustomTimeInput(forms.TimeInput):
    input_type = 'time'

class FranjaHorariaForm(forms.ModelForm):

    hora_inicio = forms.TimeField(widget=CustomTimeInput)
    hora_finalizacion = forms.TimeField(widget=CustomTimeInput)

    class Meta:
        model = FranjaHoraria
        fields = (
            'punto_acceso',
            'hora_inicio',
            'hora_finalizacion',
            'empleado',
            'is_active'
        )

    def __init__(self, empleado=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-franjaHorariaForm'
        self.helper.form_class = 'container'
        self.helper.form_method = 'post'
        self.helper.label_class = 'custom-control-label'
        # self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Enviar', css_class='btn btn-primary mt-4'))

        self.fields['punto_acceso'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['hora_inicio'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['hora_finalizacion'].widget.attrs['class'] = 'form-control form-control-solid'
        self.fields['empleado'].widget.attrs['class'] = 'form-control form-control-solid'

        self.fields['punto_acceso'].queryset = self.fields['punto_acceso'].queryset.filter(empresa=get_current_user().empresa)
        if empleado:
            self.initial['empleado'] = empleado
            self.fields['empleado'].widget = forms.HiddenInput()
