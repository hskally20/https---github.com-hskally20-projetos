# routing.py

from django.urls import re_path
from . import consumers  # Certifique-se de importar o consumer correto

# Defina a URL de WebSocket correta
websocket_urlpatterns = [
    re_path(r'ws/paciente_notifications/$', consumers.PacienteConsumer.as_asgi()),
]
