from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json
import asyncio
from django.conf import settings
import time

from chat.models import Message

from django.contrib.auth import get_user_model

User = get_user_model()

class OnlineConsumer(AsyncWebsocketConsumer):
    connected_client = {}
    async def connect(self):
        self.user = await self.get_user(self.scope['user'].username)
        self.connect_status_time = int(time.time())

        self.room = 'online'

        await self.channel_layer.group_add(
            self.room,
            self.channel_name
        )

        await self.accept()

        self.connected_client[self.user.username] = True

        self.send_connected_clients_task = asyncio.ensure_future(self.send_connected_clients_periodically(), loop=asyncio.get_event_loop())

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room, self.channel_name)
        self.disconnect_status_time = int(time.time())

        del self.connected_client[self.user.username]

        if hasattr(self, 'send_connected_clients_task'): self.send_connected_clients_task.cancel()

    async def send_connected_clients(self):
        filtered_connected_clients = {
            username: is_connected
            for username, is_connected in self.connected_client.items()
            if username != self.user.username
        }

        await self.send(text_data=json.dumps({
            'username': self.user.username,
            'connected_clients': filtered_connected_clients,
        }))


    async def send_connected_clients_periodically(self):
        while True:
            await asyncio.sleep(getattr(settings, 'UPDATE_USER_STATUS_SECONDS', 30))
            await self.send_connected_clients()

    async def uptime(self): return self.disconnect_status_time - self.connect_status_time

    @database_sync_to_async
    def get_user(self, username): return User.objects.get(username=username)

