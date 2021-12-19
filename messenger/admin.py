from django.contrib import admin

from messenger.models import Chat, Message


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'id']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['get_author', 'chat', 'id']
