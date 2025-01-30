from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.created_at
