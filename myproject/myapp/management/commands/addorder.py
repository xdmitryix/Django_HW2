from django.core.management.base import BaseCommand
from myapp.models import Order, Client, Product
from random import choice, randint


class Command(BaseCommand):
    help = "Create Order"

    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            clients = choice(Client.objects.all())
            num_products = randint(1, 5)
            products = set(choice(Product.objects.all()) for _ in range(num_products))
            total_price = sum(product.price for product in products)

            order = Order(client=clients,
                          total_price=total_price
                          )
            order.save()
            order.product.set(products)
            order.save()
            self.stdout.write(f'{order}')
