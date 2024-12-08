from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError(_("The phone number must be set"))
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_verified", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(phone, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=11, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.phone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    family = models.CharField(
        max_length=255, null=True, blank=True, default='')
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.phone


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    ostan = models.CharField(max_length=255)
    shahr = models.CharField(max_length=255)
    postcode = models.IntegerField(default=None)

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
