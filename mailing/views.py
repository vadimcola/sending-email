from django.shortcuts import render
from django.views.generic import ListView

from mailing.models import Setting


class SettingListViews(ListView):
    model = Setting



