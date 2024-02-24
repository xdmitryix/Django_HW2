from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = 'Update Product'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='product ID')
        parser.add_argument('title', type=str, help='product title')
        parser.add_argument('description', type=str, help='product description')
        parser.add_argument('price', type=int, help='product price')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        title = kwargs['title']
        description = kwargs['description']
        price = kwargs['price']
        product = Product.objects.filter(pk=pk).first()
        product.title = title
        product.description = description
        product.price = price
        product.save()
        self.stdout.write(f'{product}')