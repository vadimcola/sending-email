from mailing.models import Setting


def daily_send():
    for item in Setting.objects.filter(frequency_mailing='OPD'):
        item.mailing_status = 'active'
        item.save()
        send_newsletter(item)
        item.mailing_status = 'closed'
        item.save()


def weekly_send():
    for item in Setting.objects.filter(frequency_mailing='OPW'):
        item.mailing_status = 'active'
        item.save()
        send_newsletter(item)
        item.mailing_status = 'closed'
        item.save()


def monthly_send():
    for item in Setting.objects.filter(frequency_mailing='OPM'):
        item.mailing_status = 'active'
        item.save()
        send_newsletter(item)
        item.mailing_status = 'closed'
        item.save()


def send_newsletter(object: Client):
    emails = [client.email for client in object.client.all()]
    send_mail(
        subject=self.object.message,
        message=self.object.message.message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=emails

    )

