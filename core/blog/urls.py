from django.urls import path
from .views import BlogView

urlpatterns = [
    path('', BlogView.as_view(), name='blog-list'),
    path('<int:pk>', BlogView.as_view(), name='blog-detail')
]
