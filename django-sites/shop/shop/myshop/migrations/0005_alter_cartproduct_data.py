# Generated by Django 3.2.3 on 2021-05-27 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0004_cartproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='data',
            field=models.TextField(blank=True, null=True, verbose_name='Данные'),
        ),
    ]
