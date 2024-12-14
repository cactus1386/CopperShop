from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderHistoryViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'order', OrderViewSet, basename='order')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('order-history', OrderHistoryViewSet.as_view(), name='order-history'),
]
