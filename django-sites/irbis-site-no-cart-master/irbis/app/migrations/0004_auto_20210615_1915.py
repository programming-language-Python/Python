# Generated by Django 3.1.7 on 2021-06-15 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210613_2035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders_number',
            options={'ordering': ['id'], 'verbose_name': 'Номер заказа', 'verbose_name_plural': 'Номера заказов'},
        ),
        migrations.AddField(
            model_name='numbers',
            name='title',
            field=models.CharField(default=1, max_length=150, verbose_name='Наименование'),
            preserve_default=False,
        ),
    ]
