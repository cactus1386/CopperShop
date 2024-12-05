from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.save()  # Save the Order instance to get a primary key
        super().save_model(request, obj, form, change)


admin.site.register(Order, OrderAdmin)
