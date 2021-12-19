from django.db.models import Q, Max, Min
from rest_framework import viewsets

from .mixins import MessageMixin
from .serializers import ChatDetailSerializer, ChatListSerializer, MessageSerializer
from ..models import *


class ChatViewSet(MessageMixin, viewsets.ModelViewSet):

    def get_queryset(self):
        user = self.request.user
        not_null_chats = user.chat_set.filter(~Q(message=None))
        ordered_chats = not_null_chats.annotate(last_up=Max('message__pub_date')).order_by('-last_up')
        return ordered_chats

    def get_serializer_class(self):
        if self.action == 'list':
            return ChatListSerializer
        return ChatDetailSerializer


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return self.request.user.message_set.all()
