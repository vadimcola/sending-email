from django.core.mail import send_mail

from config import settings
from mailing.models import Setting, Client


def daily_send():
    for item in Setting.objects.filter(frequency_mailing='OPD'):
        if item.mailing_status == 'active' or 'created':
            item.save()
            send_newsletter(item)
            item.mailing_status = 'active'
            item.save()


def weekly_send():
    for item in Setting.objects.filter(frequency_mailing='OPW'):
        if item.mailing_status == 'active' or 'created':
            item.save()
            send_newsletter(item)
            item.mailing_status = 'active'
            item.save()


def monthly_send():
    for item in Setting.objects.filter(frequency_mailing='OPM'):
        if item.mailing_status == 'active' or 'created':
            item.save()
            send_newsletter(item)
            item.mailing_status = 'active'
            item.save()


def send_newsletter(object: Client):
    emails = [client.email for client in object.client.all()]
    send_mail(
        subject=object.message,
        message=object.message.message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=emails

    )

