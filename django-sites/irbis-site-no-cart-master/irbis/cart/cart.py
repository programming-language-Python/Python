from decimal import Decimal
from django.conf import settings
from django.apps import apps
from app.models import Numbers, Service, Excursion, Menu, Orders
from django.contrib.sessions.models import Session


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
            if not Orders.objects.select_related('user').filter(user_id=user_id):
                cart_product = Orders()
                cart_product.key = self.session.session_key
                cart_product.user_id = user_id
                cart_product.save()
                cart = {}
            else:
                cart_product = Orders.objects.select_related(
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
        # ! добавить slug для каждого товара. Вместо него используется title
        # * получение объектов product и добавление их в корзину
        cart = self.cart.copy()
        # list
        for model in self.cart.keys():
            Product = apps.get_model('app', model)
            for product_model in self.cart.values():
                products = Product.objects.filter(
                    title__in=product_model.keys())
                for product in products:
                    self.cart[model][product.title]['product'] = product

        for items in self.cart.values():
            for item in items.values():
                item['price'] = Decimal(item['price'])
                item['total_price'] = item['price'] * item['quantity']
                yield item

    def __len__(self):
        """
        Считаем сколько товаров в корзине
        """
        # if self.cart:
        # model_values = []
        # get_total_quantity = []

        # for value in self.cart.values():
        #     model_values.append(value.values())

        # for value in model_values[0]:
        #     get_total_quantity.append(value['quantity'])

        # return sum(get_total_quantity)

        return sum(item['quantity'] for items in self.cart.values() for item in items.values())

    # * update_quantity - нужно ли изменить количество товаров на новое(True) или добавить его к существующему(False)
    def add(self, product_model, product, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        # * преобразование в строку т.к. Django использует JSON для серилизации сессии.
        # * В JSON ключами могут быть только строки
        product_id = str(product.id)
        if product_model not in self.cart or product.title not in self.cart[product_model]:
            if product_model not in self.cart:
                self.cart[product_model] = {}
            self.cart[product_model][str(product.title)] = {'product_id': product_id, 'quantity': 0,
                                                            'price': str(product.price)}

        if update_quantity:
            self.cart[product_model][str(product.title)]['quantity'] = quantity
        else:
            self.cart[product_model][str(
                product.title)]['quantity'] += quantity

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

    def remove(self, product_model, product):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        if product_model in self.cart and product.title in self.cart[product_model]:
            if is_authenticated:
                if len(self.cart[product_model]) != 1:
                    del self.cart[product_model][product.title]
                else:
                    del self.cart[product_model]
                cart_product.data = self.cart
                cart_product.save()
            else:
                del self.cart[product_model][product.title]
                self.save()


    def get_total_price(self):
        # * получаем общую стоимость
        # model_values = []
        # get_total_price = []
        # print(self.cart.values())
        # for value in self.cart.values():
        #     model_values.append(value.values())
        # # print(model_values)
        # for value in model_values:
        #     print(value[0])
            # total_product_price = Decimal(value['price']) * value['quantity']
            # get_total_price.append(total_product_price)
        # print(get_total_price)
        # print(sum(get_total_price))
        # return sum(get_total_price)
        # return 78
        return sum(Decimal(item['price']) * item['quantity'] for items in self.cart.values() for item in items.values())

    def clear(self):
        # * очищаем корзину в сессии
        del self.session[settings.CART_SESSION_ID]
        self.save()
