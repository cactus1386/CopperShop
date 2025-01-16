from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(Blog, BlogAdmin)
