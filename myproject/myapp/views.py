from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from .models import Client, Order, Product
from django.http import HttpResponse, HttpRequest
from datetime import date, timedelta
from .forms import ImageForm



def orders_get(request: HttpRequest, client_id):
    client = Client.objects.filter(id=client_id).first()
    orders = Order.objects.filter(client=client_id)
    return render(request, 'myapp/orders_by_user.html', {'orders': orders, 'client': client})


def week_orders(request: HttpRequest, client_id):
    today = date.today()
    start_day = today - timedelta(days=7)
    client = Client.objects.filter(id=client_id).first()
    orders = Order.objects.filter(client=client, date_add__range=[start_day, today])
    products = Product.objects.filter(order__in=orders).order_by('date_add')
    products_set = set(products)
    return render(request, 'myapp/week.html', {'products_set': products_set, 'client': client})


def month_orders(request: HttpRequest, client_id):
    today = date.today()
    start_day = today - timedelta(days=30)
    client = Client.objects.filter(id=client_id).first()
    orders = Order.objects.filter(client=client, date_add__range=[start_day, today])
    products = Product.objects.filter(order__in=orders).order_by('date_add')
    products_set = set(products)
    return render(request, 'myapp/month.html', {'products_set': products_set, 'client': client})


def year_orders(request: HttpRequest, client_id):
    today = date.today()
    start_day = today - timedelta(days=365)
    client = Client.objects.filter(id=client_id).first()
    orders = Order.objects.filter(client=client, date_add__range=[start_day, today])
    products = Product.objects.filter(order__in=orders).order_by('date_add')
    products_set = set(products)
    return render(request, 'myapp/year.html', {'products_set': products_set, 'client': client})


def image_add_by_user(request, product_id):
    product = Product.objects.get(pk=product_id)

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product.photo = image
            product.save()
            print(f'Файл добавлен')
            return render(request, 'myapp/image.html', {'form': form})
    else:
        form = ImageForm()
    return render(request, 'myapp/image.html', {'form': form})

