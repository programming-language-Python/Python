from django.db import models
from django.urls import reverse
from django.conf import settings
# from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe


# Create your models here.
class Numbers(models.Model):
    class Enum(models.TextChoices):
        one = '1', _('1-но комнатный')
        two = '2', _('2-х комнатный')
        three = '3', _('3-х комнатный')
        four = '4', _('4-х комнатный')

    enum = models.CharField(
        max_length=1, choices=Enum.choices, default=Enum.one, )
    title = models.CharField(max_length=150, verbose_name='Наименование')
    subscrible = models.TextField(verbose_name='Описание')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена')
    img = models.ImageField(upload_to='photos/Номера/',
                            verbose_name='Фото')

    def del_html_tag_in_subscrible(self):
        return mark_safe(self.subscrible)

    def get_absolute_url(self):
        return reverse('app:card_numbers', kwargs={"number_id": self.pk})

    def __str__(self):
        return str(self.id)

    # для админки
    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'
        ordering = ['id']


class Service(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['id']


class Excursion(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    subscrible = models.TextField(verbose_name='Описание')
    program = models.TextField(verbose_name='Программа')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена')
    img = models.ImageField(upload_to='photos/Экскурсии/',
                            verbose_name='Фото')

    def del_html_tag_in_subscrible(self):
        return mark_safe(self.subscrible)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('app:card_excursion', kwargs={"excursion_id": self.pk})

    class Meta:
        verbose_name = 'Экскурссия'
        verbose_name_plural = 'Экскурссии'
        ordering = ['id']


class Menu(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    subscrible = models.TextField(verbose_name='Описание')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена')
    img = models.ImageField(upload_to='photos/Меню/',
                            verbose_name='Фото')

    def del_html_tag_in_subscrible(self):
        return mark_safe(self.subscrible)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('app:card_menu', kwargs={"menu_id": self.pk})

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['id']


class Order_numbers(models.Model):
    data = models.JSONField(verbose_name='Заказано')
    count = models.IntegerField(default=0, verbose_name='Количество товаров')
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена')
    date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата заказа')
    user = models.ForeignKey(
        'Orders', on_delete=models.PROTECT, verbose_name='Заказчик')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Номер заказа'
        verbose_name_plural = 'Номера заказов'
        ordering = ['id']


class Orders(models.Model):
    # number_id = models.ForeignKey(
    #     Numbers, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Id номера')
    # service_id = models.ForeignKey(
    #     Service, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Id услуги')
    # excursion_id = models.ForeignKey(
    #     Excursion, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Id экскурсии')
    # menu_id = models.ForeignKey(
    #     Menu, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Id меню')
    # user_id = models.ForeignKey(
    #     User, on_delete=models.PROTECT, verbose_name='Пользователь')
    # orders_number_id = models.ForeignKey(
    #     Orders_number, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Id заказа')
    key = models.TextField(verbose_name='Ключ')
    data = models.JSONField(null=True, blank=True, verbose_name='Данные')
    count = models.IntegerField(default=0, verbose_name='Покупки')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cartProducts',
                             on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['id']
