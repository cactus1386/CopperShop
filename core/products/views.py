from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, ListAPIView
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class ProductList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'price']
    search_fields = ["name", "description"]
    ordering_fields = ["created_at"]


class ProductDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CategoryList(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TopDiscountsList(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(discount__gt=0).order_by('-discount')[:10]
