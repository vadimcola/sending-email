from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import SettingListViews, SettingCreateView, SettingDetailView, SettingUpdateView, SettingDeleteView, \
    LogListView, LogDetailView, IndexView

app_name = MailingConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index_list'),
    path('setting/', SettingListViews.as_view(), name='setting_list'),
    path('setting/create/', SettingCreateView.as_view(), name='setting_create'),
    path('setting/<int:pk>', SettingDetailView.as_view(), name='setting_detail'),
    path('setting/update/<int:pk>/', SettingUpdateView.as_view(), name='setting_update'),
    path('setting/delete/<int:pk>/', SettingDeleteView.as_view(), name='setting_delete'),
    path('log/', LogListView.as_view(), name='log_list'),
    path('log/<int:pk>/', LogDetailView.as_view(), name='log_details')
]
