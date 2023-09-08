from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json

from chat.models import Message

from django.contrib.auth import get_user_model

User = get_user_model()

class TypingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        my_id = int(self.scope['user'].id)
        other_user_id = int(self.scope['url_route']['kwargs']['id'])

        if my_id > other_user_id:
            self.room_name = f'{my_id}-{other_user_id}'
        else:
            self.room_name = f'{other_user_id}-{my_id}'

        self.room_group_name = 'typing_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        sender_username = text_data_json['sender_username']
        typing = text_data_json['typing']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'show.typing',
                'sender_username': sender_username,
                'typing': typing,
                'sender_channel_name': self.channel_name,
            }
        )

    async def show_typing(self, event):
        sender_username = event['sender_username']
        typing = event['typing']
        sender_channel_name = event['sender_channel_name']

        if self.channel_name != event['sender_channel_name']:
            await self.send(text_data=json.dumps({
                'sender_username': sender_username,
                'typing': typing,
            }))
