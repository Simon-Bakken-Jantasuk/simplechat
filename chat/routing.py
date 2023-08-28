from django.urls import path

from chat.consumers import ChatConsumer, TypingConsumer

websocket_urlpatterns = [
    path('ws/chat/<int:id>/', ChatConsumer.as_asgi()),
    path('ws/chat/<int:id>/typing/', TypingConsumer.as_asgi()),
]
