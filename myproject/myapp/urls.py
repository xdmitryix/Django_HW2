from django.urls import path
from . import views

urlpatterns = [
    path('orders/<int:client_id>/', views.orders_get, name='orders_get'),
    path('week/<int:client_id>/', views.week_orders, name='week_orders'),
    path('month/<int:client_id>/', views.month_orders, name='month_orders'),
    path('year/<int:client_id>/', views.year_orders, name='year_orders'),
    path('image/<int:product_id>/', views.image_add_by_user, name='image_add_by_user'),
]
