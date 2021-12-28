# Generated by Django 3.1.7 on 2021-08-03 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_count', models.IntegerField(default=0, verbose_name='Общее количество')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Общая сумма')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'cart',
                'verbose_name_plural': 'carts',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Order_numbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField(verbose_name='Заказано')),
                ('count', models.IntegerField(default=0, verbose_name='Количество товаров')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')),
                ('checked_out', models.BooleanField(default=False, verbose_name='checked out')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cart.cart', verbose_name='Заказчик')),
            ],
            options={
                'verbose_name': 'Номер заказа',
                'verbose_name_plural': 'Номера заказов',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_product', models.CharField(choices=[('Номер', 'Номер'), ('Услуга', 'Услуга'), ('Экскурсии', 'Экскурсии'), ('Меню', 'Меню')], default='Меню', max_length=25)),
                ('quantity', models.PositiveIntegerField(verbose_name='quantity')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='unit price')),
                ('object_id', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart', verbose_name='cart')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'items',
                'ordering': ('cart',),
            },
        ),
    ]
