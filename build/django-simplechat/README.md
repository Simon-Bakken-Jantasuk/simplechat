#### Simplechat 

Simplechat is a Django app to where one could easily add chatting functionality.
It is supposed to be customizable and easy to use.

Detailed documentation is in the `docs` directory.

#### Quick start

1. Add this into your `settings.py` like this:
    ```python
    INSTALLED_APPS = [
        ...,
        'chat',
    ]
   
   ASGI_APPLICATION = 'mysitename.asgi.application'
   CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels.layers.InMemoryChannelLayer', # For quick start, use in-memory channel layer. For production, use Redis or similar.
        },
    }
    ```

2. Include the chat URLconf in your project `urls.py` like this:
    ```python 
    path("chat/", include("chat.urls")),`
    ```

3. Include this into your `asgi.py` like this:
   ```python
    ...

    from channels.auth import AuthMiddlewareStack
    from channels.routing import ProtocolTypeRouter, URLRouter
    from channels.security.websocket import AllowedHostsOriginValidator
    from django.urls import re_path, path

    ...

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
    ```

5. Run `python manage.py migrate` to create the chat models.

6. Start the development server, login or register if you have no account, then visit `http://127.0.0.1:8000/chat/` to chat with users.
