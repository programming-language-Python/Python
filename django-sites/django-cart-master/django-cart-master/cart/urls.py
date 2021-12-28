from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', get_cart, name='cart_detail'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
]
