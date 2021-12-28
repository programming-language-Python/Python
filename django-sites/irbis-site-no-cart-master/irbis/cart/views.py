from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.apps import apps
from .cart import Cart
from .forms import CartAddProductForm
from app.models import Orders, Order_numbers
import datetime
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@require_POST
def cart_add(request, product_model, product_id):
    # * Берём модель в которой находится товар
    Product = apps.get_model('app', product_model)
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product_model=product_model,
                 product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_model, product_id):
    Product = apps.get_model('app', product_model)
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product_model, product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})


def cart_order_numbers(request, get_total_price):
    if request.method == 'POST':
        cart = Cart(request)
        subject = 'Спасибо за совершение покупки на сайте Pink irbis!'
        html_message = render_to_string(
            'inc/mail_template.html', {'cart': cart, 'len': cart.__len__()})
        plain_message = strip_tags(html_message)
        from_email = 'Pink irbis <{}>'.format(settings.EMAIL_HOST_USER)

        mail = send_mail(subject, plain_message, from_email,
                         [request.user.email], html_message=html_message)
        if mail:
            order = Orders.objects.get(user=request.user)
            order_number = Order_numbers.objects.create(data=order.data, count=cart.__len__(), price=get_total_price, user=order)
            order.data = {}
            order.count += 1
            order.save()
        # очистка корзины
        # cart.clear()
        return render(request, 'cart/detail.html', {'purchase_is_perfect': 1})
