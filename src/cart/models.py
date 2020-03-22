from django.db import models
from django.conf import settings
from django.utils import timezone

from checkout.models import Address
from products.models import Product
User = settings.AUTH_USER_MODEL

class CartItem(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product    = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity   = models.IntegerField(default=1)
    ordered    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.product.title

    def total_item_price(self):
        return (self.product.current_price * self.quantity)

    def total_item_discount(self):
        if self.product.old_price:
            return ((self.product.old_price - self.product.current_price) * self.quantity)
        else:
            return 0




"""
1- add item to cart
2- adding billing adress
3- payment
4- being delivered
5- received
6- refunds
"""
class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    products = models.ManyToManyField(CartItem)

    code    = models.CharField(max_length= 25)
    ordered = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    ordered_at = models.DateTimeField(default = timezone.now)

    shipping_address = models.ForeignKey(Address, related_name='shipping_address', on_delete= models.CASCADE, null=True, blank=True)
    billing_address  = models.ForeignKey(Address, related_name='billing_address', on_delete= models.CASCADE, null=True, blank=True)

    in_way   = models.BooleanField(default=False)
    received = models.BooleanField(default=False)

    refund_requested = models.BooleanField(default=False)
    refund_granted   = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username




    def total_order_price(self):
        total = 0
        for product in self.products.all():
            total += product.total_item_price()
        return total


    def total_item_discount(self):
        total = 0
        for product in self.products.all():
            total += product.total_item_discount()
        return total
