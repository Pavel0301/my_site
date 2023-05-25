from django.contrib import admin

from discussions.models import Discussion




@admin.register(Discussion)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'date_updated', 'author',]
    prepopulated_fields = {'slug': ['title']}