
from django.db import models
from django.contrib.auth import get_user_model
from django.views.generic.edit import ProcessFormView

# Create your models here.

from books.models import Book
from users.models import Employee

User = get_user_model()

from books import models as books_models

class Cart(models.Model):
    customer = models.ForeignKey(User, null=True, blank=True, related_name='carts', verbose_name="Корзина", on_delete=models.PROTECT)

    @property
    def total_price(self):
        total_price = 0
        goods = self.goods.all()
        for good in goods:
            total_price += good.total_price
        return total_price

    # def __str__(self):
    #     return super().__str__()

class BooksInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Cart', related_name='goods')
    book = models.ForeignKey('books.Book', on_delete=models.PROTECT, verbose_name='Book')
    quantity = models.IntegerField(verbose_name='Quantity', default=1)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Unit price')
    
    @property
    def total_price(self):
        return self.unit_price*self.quantity