from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    client_name = models.CharField(max_length=255, **NULLABLE, verbose_name='ФИО Клиента')
    email = models.EmailField(unique=True, verbose_name='Почта')
    comment = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.email}'


class Message(models.Model):
    subject_message = models.CharField(max_length=255, **NULLABLE,
                                       verbose_name='Тема сообщения')
    message = models.TextField(**NULLABLE, verbose_name='Сообщение')
    mailing_time = models.DateTimeField(verbose_name='Время отправки')

