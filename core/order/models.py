from django.db import models
from django.conf import settings
from products.models import Product
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="order_items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)


@receiver(pre_save, sender=Order)
def update_total(sender, instance, **kwargs):
    instance.total = sum(
        item.price * item.quantity for item in instance.order_items.all())
