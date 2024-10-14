# asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import cadastros.routing  # Certifique-se de ajustar o caminho para o seu arquivo routing.py

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meuprojeto.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            myapp.routing.websocket_urlpatterns  # Defina a URL para WebSockets no routing.py
        )
    ),
})
