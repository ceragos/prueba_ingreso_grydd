from django import forms


class BaseModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control form-control-solid'})
        for field in self.errors:
            self.fields[field].widget.attrs.update({'class': 'form-control form-control-solid is-invalid'})
