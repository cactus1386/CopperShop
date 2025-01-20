from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.


class BlogView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class BlogDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
