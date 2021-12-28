from .cart import Cart
from myshop.models import Product
from django.shortcuts import render


def add_to_cart(request, product_id, quantity=1):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.unit_price, quantity)
    return render(request, 'cart/cart.html', {'cart': Cart(request)})


def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return render(request, 'cart/cart.html', {'cart': Cart(request)})


def get_cart(request):
    return render(request, 'cart/cart.html', {'cart': Cart(request)})
