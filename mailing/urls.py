from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import SettingListViews

app_name = MailingConfig.name

urlpatterns = [
    path('', SettingListViews.as_view(), name='setting_list'),
]