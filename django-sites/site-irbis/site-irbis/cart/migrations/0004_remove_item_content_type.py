# Generated by Django 3.1.7 on 2021-08-03 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_remove_cart_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='content_type',
        ),
    ]
