from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from config import settings
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

    def form_valid(self, form):
        self.object = form.save()

        send_mail(
            subject='Поздравляем c регистрацией',
            message=f'Для завершения регистрации пройдите по ссылке',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list={'vadimcola@mail.ru'}
        )
        return super().form_valid(form)


class SettingUpdateView(UpdateView):
    model = Setting
    form_class = SettingForm
    success_url = reverse_lazy('mailing:setting_list')


class SettingDeleteView(DeleteView):
    model = Setting
    success_url = reverse_lazy('mailing:setting_list')
    template_name = 'mailing/setting_confirm_delete.html'
