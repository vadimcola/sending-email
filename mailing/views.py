from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

import mailing
from config import settings
from mailing.forms import SettingForm
from mailing.models import Setting, Log
from mailing.services import send_newsletter


class IndexView(LoginRequiredMixin, ListView):
    def get(self, request, *args, **kwargs):
        context = {
            'title': 'Главная',

        }
        return render(request, 'mailing/index.html', context)


class SettingListViews(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Setting
    permission_required = 'mailing.view_setting'

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset = queryset.filter()

        return queryset


class SettingDetailView(LoginRequiredMixin, DetailView):
    model = Setting
    template_name = 'mailing/setting_detail.html'


class SettingCreateView(LoginRequiredMixin, CreateView):
    model = Setting
    form_class = SettingForm
    template_name = 'mailing/setting_form.html'
    success_url = reverse_lazy('mailing:setting_list')

    def form_valid(self, form):
        self.object = form.save()
        if self.object.mailing_status in ('active', 'created'):
            send_newsletter(self.object)

        self.object.owner = self.request.user
        self.object.save()
        self.object.mailing_status = 'created'
        self.object.save()
        return super().form_valid(form)


class SettingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Setting
    form_class = SettingForm
    success_url = reverse_lazy('mailing:setting_list')
    permission_required = 'mailing.change_setting'


class SettingDeleteView(LoginRequiredMixin, DeleteView):
    model = Setting
    success_url = reverse_lazy('mailing:setting_list')
    template_name = 'mailing/setting_confirm_delete.html'


class LogListView(LoginRequiredMixin, ListView):
    model = Log


class LogDetailView(LoginRequiredMixin, DetailView):
    model = Log
    template_name = 'mailing/log_detail.html'
