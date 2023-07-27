from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import SettingListViews, SettingCreateView

app_name = MailingConfig.name

urlpatterns = [
    path('', SettingListViews.as_view(), name='setting_list'),
    path('setting/create/', SettingCreateView.as_view(), name='setting_create')
]