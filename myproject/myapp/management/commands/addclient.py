from django.core.management.base import BaseCommand
from myapp.models import Client
from random import randint


class Command(BaseCommand):
    help = "Create Client"

    def handle(self, *args, **kwargs):
        for i in range(1, 5):
            client = Client(name=f'client{i}',
                            email=f'client{i}@mail.ru',
                            phone_num=randint(80000000000, 89999999999)
                            )
            client.save()
            self.stdout.write(f'{client}')
