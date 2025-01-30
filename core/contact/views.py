from django.shortcuts import render
from .serializers import ContactSerializer
from .models import Contact
from rest_framework.generics import CreateAPIView


# Create your views here.
class ContactView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
