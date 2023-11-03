from django.contrib import admin
from .models import Post, Category


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'data_create', 'slug', 'is_published']
    list_editable = ['slug', 'is_published']
