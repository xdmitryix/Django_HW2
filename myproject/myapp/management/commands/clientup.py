from django.core.management.base import BaseCommand
from myapp.models import Client

class Command(BaseCommand):
    help = 'Update User'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Client name')
        parser.add_argument('email', type=str, help='Client email')
        parser.add_argument('phone_num', type=str, help='Client phone_num')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        name = kwargs['name']
        email = kwargs['email']
        phone_num = kwargs['phone_num']
        client = Client.objects.filter(pk=pk).first()
        client.name = name
        client.email = email
        client.phone_num = phone_num
        client.save()
        self.stdout.write(f'{client}')