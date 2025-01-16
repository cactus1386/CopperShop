from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Blog
from .serializers import BlogSerializer

# Create your views here.


class BlogView(ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
