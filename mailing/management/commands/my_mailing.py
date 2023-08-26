from django.core.management import BaseCommand

from mailing.services import send


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Принудительный запуск рассылки')
        send()
        print('Рассылка завершена')
