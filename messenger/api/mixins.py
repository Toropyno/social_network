from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework.decorators import action
from rest_framework.response import Response

from .. import services
from .serializers import ChatListSerializer, MessageSerializer, NewMessageSerializer


class ChatMixin:

    @action(detail=True, methods=['post'])
    def get_chat(self, request, pk=None):
        """
        Получает общий чат для пользователей
        """
        other_user = self.get_object()
        chat = services.get_chat(request.user, other_user)
        serializer = ChatListSerializer(chat, context={'request': request})
        return Response(serializer.data)


class MessageMixin:

    @action(detail=True, methods=['post'])
    def create_msg(self, request, pk=None):
        """
        Создает сообщение в чате
        """
        serializer = NewMessageSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
        if request.is_ajax():
            return Response()
        return redirect(request.META['HTTP_REFERER'])

    @action(detail=True)
    def get_messages(self, request, pk=None):
        """
        Получает все сообщения для чата
        """
        messages = self.get_object().message_set.all()
        serializer = MessageSerializer(messages, many=True, context={'request': request})
        return Response(serializer.data)
