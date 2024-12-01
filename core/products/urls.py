from django.urls import path, include
from .views import ProductList, ProductDetail, CategoryList, TopDiscountsList

app_name = "shop"


urlpatterns = [
    path("", ProductList.as_view(), name="product-list"),
    path(
        "<int:pk>",
        ProductDetail.as_view(),
        name="product-detail",
    ),
    path('category/', CategoryList.as_view(), name="category"),
    path('top-discounts/', TopDiscountsList.as_view(), name='top-discounts'),
]
