from django.db.models import Q

from main_app.api.serializers import UserSerializer
from .models import *


def get_chat(user1, user2):
    """
    Получает общий чат для пользователей
    """
    chat, created = Chat.objects.filter(members=user1).filter(members=user2).get_or_create()
    if created:
        chat.members.add(user1, user2)
    return chat


def get_chat_client(chat, request):
    """
    Получает собеседника в чате
    """
    return chat.members.exclude(pk=request.user.pk).first()
