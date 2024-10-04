from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/sala/<int:paciente_id>/', consumers.NotificacaoConsumer.as_asgi()),
]
