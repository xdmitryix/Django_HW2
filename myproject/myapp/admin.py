from django.contrib import admin
from .models import Product, Client, Order


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['title', 'price', 'date_add']
    list_filter = ['price', 'date_add']
    ordering = ['price', 'date_add']
    search_fields = ['description']
    readonly_fields = ['date_add']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Подробности:',
            {
                'classes': ['collapse'],
                'description': 'Подробное описание товара:',
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия:',
            {
                'fields': ['price'],
            }
        ),
        (
            'Данные:',
            {
                'description': 'Дата создания заказа:',
                'fields': ['date_add'],
            }
        ),
        (
            'Фото:',
            {
                'description': 'Изобрвжение товара:',
                'fields': ['photo'],
            }
        ),
    ]


class ClientAdmin(admin.ModelAdmin):
    """Список клиентов."""
    list_display = ['name', 'email', 'phone_num', 'registration_date']
    list_filter = ['name', 'registration_date']
    ordering = ['name', 'registration_date']
    search_fields = ['name', 'phone_num', 'email']
    fields = ['name', 'email', 'phone_num']
    readonly_fields = ['registration_date']


class OrderAdmin(admin.ModelAdmin):
    """Список заказов."""
    list_display = ['client', 'total_price', 'date_add']
    list_filter = ['client', 'total_price', 'date_add']
    ordering = ['client', 'total_price', 'date_add']
    search_fields = ['date_add']
    fields = ['client', 'product']
    readonly_fields = ['total_price', 'date_add']


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
