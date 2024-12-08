from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.category


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    pic = models.ImageField(upload_to='uploads/')
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    brand = models.CharField(max_length=255, blank=True,
                             null=True, default="mes")
    category = models.ForeignKey(
        Category, related_name='product', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_api_url(self):
        return reverse("shop:product-detail", kwargs={"pk": self.pk})


class Images(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images_set"
    )
    image = models.ImageField(upload_to='uploads/')
