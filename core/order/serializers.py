from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(
        many=True, read_only=True, source='order_items')
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'user', 'created_at', 'updated_at', 'items', 'total')

    def get_total(self, obj):
        return sum(item.price * item.quantity for item in obj.order_items.all())
