from django.core.management.base import BaseCommand
from myapp.models import Order


class Command(BaseCommand):
    help = 'Get all Orders'

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        self.stdout.write(f'Список всех заказов: {orders}')