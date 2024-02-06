from django.core.management.base import BaseCommand
from myapp.models import Product

class Command(BaseCommand):

    help = 'Get all Products'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        self.stdout.write(f'Список всех продуктов: {products}')