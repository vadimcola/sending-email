from django.db import models
from django.utils import timezone

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

    def __str__(self):
        return f'{self.subject_message}'


class Setting(models.Model):

    FREQUENCY = [
        (None, 'Не указано'),
        ('OPD', 'Раз в день'),
        ('OPW', 'Раз в неделю'),
        ('OPM', 'Раз в месяц')
    ]

    STATUS = [
        (None, 'Не указано'),
        ('created', 'Создана'),
        ('active', 'Запущена'),
        ('closed', 'Завершена')
    ]
    mailing_time = models.DateTimeField(default=timezone.now, verbose_name='Время отправки')
    frequency_mailing = models.CharField(max_length=3, choices=FREQUENCY,
                                         verbose_name='Переодичность отправки')
    mailing_status = models.CharField(max_length=7, choices=STATUS,
                                      verbose_name='Статус отправки')
