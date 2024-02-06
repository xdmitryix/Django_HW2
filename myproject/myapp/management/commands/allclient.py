from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = 'Get all Clients'

    def handle(self, *args, **kwargs):
        clietns = Client.objects.all()
        self.stdout.write(f'Список всех клиентов: {clietns}')