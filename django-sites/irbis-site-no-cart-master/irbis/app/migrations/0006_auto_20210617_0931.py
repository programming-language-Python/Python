# Generated by Django 3.1.7 on 2021-06-17 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210615_1950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders_number',
            old_name='order_date',
            new_name='date',
        ),
        migrations.AddField(
            model_name='orders_number',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Цена'),
            preserve_default=False,
        ),
    ]
