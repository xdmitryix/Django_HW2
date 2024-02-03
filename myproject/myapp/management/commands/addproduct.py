from django.core.management.base import BaseCommand
from myapp.models import Product
from random import randint


class Command(BaseCommand):
    help = "Create Product"

    def handle(self, *args, **kwargs):
        for i in range(1, 15):
            product = Product(title=f'product{i}',
                              description=f'text{i}',
                              price=randint(1000, 10000)
                              )
            product.save()
            self.stdout.write(f'{product}')
