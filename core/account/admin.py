from django.contrib import admin
from .models import User, Profile, Address
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class CustomAdmin(UserAdmin):
    model = User
    list_display = ("phone", "is_staff", "is_active", "is_verified")
    list_filter = ("phone", "is_staff", "is_active", "is_verified")
    searching_fields = ("phone",)
    ordering = ("phone",)
    fieldsets = (
        ("Authentication", {"fields": ("phone", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                )
            },
        ),
        ("group permissions", {"fields": ("groups", "user_permissions")}),
        ("login date", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                ),
            },
        ),
    )


admin.site.register(User, CustomAdmin)
admin.site.register(Profile)
admin.site.register(Address)
