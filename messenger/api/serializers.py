from django.utils import timezone
from rest_framework import serializers

from main_app.api.serializers import UserSerializer, WSUserSerializer
from ..models import *
from .. import services


class ChatListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:chat-detail', read_only=True)
    absolute_url = serializers.URLField(source='get_absolute_url')
    client = serializers.SerializerMethodField()
    last_message = serializers.CharField()
    last_update = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = Chat
        fields = [
            'id',
            'url',
            'absolute_url',
            'client',
            'last_message',
            'last_update',
        ]

    def get_client(self, obj):
        request = self.context.get('request')
        client = services.get_chat_client(obj, request)
        serializer = UserSerializer(client, context={'request': request})

        return serializer.data


class ChatDetailSerializer(serializers.ModelSerializer):
    absolute_url = serializers.URLField(source='get_absolute_url')
    client = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = [
            '__str__',
            'absolute_url',
            'client',
        ]

    def get_client(self, obj):
        request = self.context.get('request')
        client = services.get_chat_client(obj, request)
        serializer = UserSerializer(client, context={'request': request})

        return serializer.data


class MessageSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format='%H:%M', default=timezone.now())
    author = WSUserSerializer()

    class Meta:
        model = Message
        fields = [
            'chat',
            'author',
            'text',
            'pub_date',
        ]


class NewMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = [
            'chat',
            'author',
            'text',
        ]
