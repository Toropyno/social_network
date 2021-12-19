import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from messenger.api.serializers import MessageSerializer
from messenger.models import Message, Chat


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_pk = self.scope['url_route']['kwargs']['pk']
        self.chat_group_name = f'chat_{self.chat_pk}'

        await self.channel_layer.group_add(
            self.chat_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.chat_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        new_message = await self.create_new_message(text_data_json)

        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'chat_message',
                'message': MessageSerializer(new_message).data
            }
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))

    @database_sync_to_async
    def create_new_message(self, data):
        message = Message.objects.create(
            author=self.scope['user'],
            chat_id=data.get('chat'),
            text=data.get('text')
        )
        return message
