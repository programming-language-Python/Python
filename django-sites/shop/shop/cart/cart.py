from decimal import Decimal
from django.conf import settings
from myshop.models import Product, cartProduct


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        global user_id, is_authenticated, cart_product
        user_id = request.user.id
        is_authenticated = request.user.is_authenticated
        self.session = request.session
        # * Проверяем была ли у пользователя сессия
        if request.user.is_authenticated:
            # * создаём данные корзины
            if not cartProduct.objects.select_related('user').filter(user_id=user_id):
                cart_product = cartProduct()
                cart_product.key = self.session.session_key
                cart_product.user_id = user_id
                cart_product.save()
                cart = {}
            else:
                cart_product = cartProduct.objects.select_related(
                    'user').get(user_id=user_id)
                cart = cart_product.data
        else:
            # * пытаемся получить корзину с текущей сессии с помощью self.session.get(settings.CART_SESSION_ID).
            cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # * сохранить пустую корзину в сеансе
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        product_ids = self.cart.keys()
        # * получение объектов product и добавление их в корзину
        products = Product.objects.select_related(
            'category').filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            print(item)
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Считаем сколько товаров в корзине
        """
        return sum(item['quantity'] for item in self.cart.values())

    # * update_quantity - нужно ли изменить количество товаров на новое(True) или добавить его к существующему(False)
    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        # * преобразование в строку т.к. Django использует JSON для серилизации сессии.
        # * В JSON ключами могут быть только строки
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        if is_authenticated:
            cart_product.data = self.cart
            cart_product.save()
        else:
            self.save()

    def save(self):
        # * Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # * Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            if is_authenticated:
                del self.cart[product_id]
                # del cart_product.data[product_id]
                cart_product.data = self.cart
                cart_product.save()
            else:
                del self.cart[product_id]
                self.save()

    def get_total_price(self):
        # * получаем общую стоимость
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # * очищаем корзину в сессии
        del self.session[settings.CART_SESSION_ID]
        self.save()
