from django.db import models
from django.db.models.fields.related import ForeignKey

from carts.models import Cart

# Create your models here.

# class StatusOrder(models.Model):
#     status = models.CharField(verbose_name='Выбрать статус заказа', max_length=20, default='new', blank=True, null=True)

class Order(models.Model):
    cart = ForeignKey(Cart, on_delete=models.PROTECT, verbose_name="Заказ")
    status_order = models.CharField(
        max_length=20,
        default='в обработке',
        choices=[
            ('в обработке', 'в обработке'),
            ('передан курьеру', 'передан курьеру'),
            ('выполнен', 'выполнен'),
            ('отменен', 'отменен')
        ]
    )
    contact_info = models.TextField(verbose_name='Контактная информация')
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(verbose_name="Дата последнего изменения", auto_now_add=False, auto_now=True)

