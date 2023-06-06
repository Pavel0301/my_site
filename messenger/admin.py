from django.contrib import admin

import messenger

from messenger.models import Room, Message
# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Admin panel configuration for Room model."""

    list_display = ('id', 'name')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Admin panel configuration for Message model."""

    list_display = ('id', 'user', 'text', 'date')