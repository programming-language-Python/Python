from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<str:product_model>/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<str:product_model>/<int:product_id>/', cart_remove, name='cart_remove'),
    path('cart_order_numbers/<str:get_total_price>/', cart_order_numbers, name='cart_order_numbers'),
]
