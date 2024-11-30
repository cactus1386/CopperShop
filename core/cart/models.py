from django.db import models
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @receiver(post_save, sender=User)
    def create_user_cart(sender, created, instance, *args, **kwargs):
        if created:
            Cart.objects.create(user=instance)

    def get_total_price(self):
        return sum(item.product.price * item.quantity for item in self.cart_item.all())


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, related_name="cart_item", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="cart_product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
