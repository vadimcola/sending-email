from django import forms

from mailing.models import Setting


class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
