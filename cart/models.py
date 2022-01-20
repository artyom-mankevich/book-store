import decimal

from django.contrib import admin
from django.db import models

# Create your models here.
from products.models import Book
from store_project import settings


class Order(models.Model):
    order_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=13, decimal_places=4, default=0)

    def get_order_total_price(self):
        order_items = self.orderitem_set.all()
        self.total_price = sum([item.total_price for item in order_items])
        return self.total_price

    @property
    def items_count(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total

    def __str__(self):
        return ' '.join((str(self.id), str(self.order_date)))


class OrderItem(models.Model):
    quantity = models.SmallIntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)

    @property
    def total_price(self) -> decimal.Decimal:
        return self.book.price * self.quantity

    def __str__(self):
        return ' '.join((str(self.id), str(self.quantity), str(self.book.isbn)))
