from django import forms

from mailing.models import Setting


class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = '__all__'

    def _init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

