from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from mailing.forms import SettingForm
from mailing.models import Setting


class SettingListViews(ListView):
    model = Setting


class SettingDetailView(DetailView):
    model = Setting
    template_name = 'mailing/setting_detail.html'


class SettingCreateView(CreateView):
    model = Setting
    form_class = SettingForm
    template_name = 'mailing/setting_form.html'
    success_url = reverse_lazy('mailing:setting_list')




