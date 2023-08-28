import json
from common.utils.simplechat import datetime_message  
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async

from .models import Message

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        my_id = int(self.scope['user'].id)
        other_user_id = int(self.scope['url_route']['kwargs']['id'])

        if my_id > other_user_id:
            self.room_name = f'{my_id}-{other_user_id}'
        else:
            self.room_name = f'{other_user_id}-{my_id}'

        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        sender_username = text_data_json['sender_username']
        receiver_username = text_data_json['receiver_username']
        datetime_object, datetime_format = datetime_message()

        sender = await self.get_user(sender_username)
        receiver = await self.get_user(receiver_username)
        await self.save_message(self.room_group_name, sender, receiver, message, datetime_object)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': message,
                'sender_username': sender_username,
                'receiver_username': receiver_username,
                'datetime_format': datetime_format,
            }
        )

    async def chat_message(self, event):
        sender_username = event['sender_username']
        message = event["message"]
        receiver_username = event['receiver_username']
        datetime_format = event['datetime_format'] 


        await self.send(text_data=json.dumps({
            "sender_username": sender_username, 
            "message": message, 
            "receiver_username": receiver_username,  
            "datetime_format": datetime_format, 
        }))
    
    @database_sync_to_async
    def save_message(self, thread_name, sender, receiver, message, datetime_object):
        if not isinstance(datetime_object, str): datetime_object = str(datetime_object)
        return Message.objects.create(thread_name=thread_name, sender=sender, receiver=receiver, message=message, created=datetime_object)

    @database_sync_to_async
    def get_user(self, username):
        return User.objects.get(username=username)
