from django.contrib import admin

# Register your models here.

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'date_updated', 'author',]
    prepopulated_fields = {'slug': ['title']}