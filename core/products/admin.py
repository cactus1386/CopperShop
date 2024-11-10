from django.contrib import admin
from .models import Product, Category, Size, Images, Color

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Images)
