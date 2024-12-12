from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem
from .serializers import OrderSerializer
from cart.models import Cart, CartItem


class OrderViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def create_order(self, request):
        cart = Cart.objects.get(user=request.user)
        if not cart.cart_item.exists():
            return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

        # Create and save the Order instance
        order = Order(user=request.user)
        order.save()

        # Ensure the order instance has a primary key
        if not order.pk:
            return Response({'error': 'Order instance did not get a primary key'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Create OrderItem instances
        order_items = []
        for item in cart.cart_item.all():
            order_item = OrderItem(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            order_items.append(order_item)

        # Save all OrderItems at once
        try:
            OrderItem.objects.bulk_create(order_items)
        except Exception as e:
            # Clean up the order if creating order items failed
            order.delete()
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Clear the cart items
        cart.cart_item.all().delete()

        # Reset the cart total
        cart.total = 0
        cart.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
