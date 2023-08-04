import random

from django.conf import settings
from django.contrib.auth import login
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView

from users.forms import UserRegisterForm, RegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:notification')

    def form_valid(self, form):
        self.object = form.save()
        self.object.verification_key = ''.join([str(random.randint(0, 9))
                                                for _ in range(21)])

        send_mail(
            subject='Поздравляем c регистрацией',
            message=f'Для завершения регистрации пройдите по ссылке\n'
                    f'http://127.0.0.1:8000/users/verify/{self.object.verification_key}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)


class ConfirmView(TemplateView):
    def get(self, *args, **kwargs):
        key = self.kwargs.get('key')
        user = User.objects.filter(verification_key=key).first()
        if user:
            user.is_active = True
            user.verification_key = key
            user.save()
            login(self.request, user)

        return redirect('users:reg_success')


class UserUpdateView(UpdateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(subject='Вы сменили пароль',
              message=f'Ваш новый пароль: {new_password}',
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[request.user.email]
              )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('main:prod_list'))