import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificacaoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.paciente_id = self.scope['url_route']['kwargs']['paciente_id']
        self.sala_grupo = f'notificacao_{self.paciente_id}'

        # Junte-se ao grupo
        await self.channel_layer.group_add(
            self.sala_grupo,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Saia do grupo
        await self.channel_layer.group_discard(
            self.sala_grupo,
            self.channel_name
        )

    # Recebe mensagem do WebSocket
    async def receber_notificacao(self, event):
        message = event['message']

        # Envia mensagem para WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
