from django.urls import path

from chat.consumers import ChatConsumer, TypingConsumer, OnlineConsumer

websocket_urlpatterns = [
    path('ws/chat/<int:id>/', ChatConsumer.as_asgi()),
    path('ws/chat/<int:id>/typing/', TypingConsumer.as_asgi()),
    path('ws/chat/online/', OnlineConsumer.as_asgi()),
]
