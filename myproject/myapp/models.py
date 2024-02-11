from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_num = models.CharField(max_length=20)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'name: {self.name}, email: {self.email}, phone number: {self.phone_num},'
                f' registration date: {self.registration_date}')


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_add = models.DateField(auto_now_add=True)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return (f'title: {self.title}, description: {self.description}, price: {self.price},'
                f' date_add: {self.date_add}')

    def get_date(self):
        return self.date_add


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f'client: {self.client}, product: {self.product}, total_price: {self.total_price},'
                f' date_add: {self.date_add}')

