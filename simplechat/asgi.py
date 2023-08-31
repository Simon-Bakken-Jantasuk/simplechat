import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import re_path, path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simplechat.settings")
django_asgi_app = get_asgi_application()

from chat.consumers import * 

application = ProtocolTypeRouter({
    "http": django_asgi_app,

    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path('ws/chat/<int:id>/', ChatConsumer.as_asgi()),
            ])
        )
    ),
})
