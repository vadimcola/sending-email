from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from users.apps import UsersConfig
from users.views import RegisterView, UserUpdateView, ConfirmView, generate_new_password

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/notification/',
         TemplateView.as_view(template_name='users/reg_notification.html'), name='notification'),
    path('verify/<key>/', ConfirmView.as_view(), name='confirm'),
    path('reg-success/', TemplateView.as_view(template_name='users/reg_success.html'), name='reg_success'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/gen-password', generate_new_password, name='generate_new_password')
]