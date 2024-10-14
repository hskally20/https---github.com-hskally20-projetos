# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class PacienteConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Criação de um canal único por usuário ou por grupo de pacientes
        self.room_name = "paciente_notifications"  # Pode ser personalizado
        self.room_group_name = f'paciente_{self.room_name}'

        # Adiciona o cliente ao grupo
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Confirma a conexão WebSocket
        await self.accept()

    async def disconnect(self, close_code):
        # Remove o cliente do grupo
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Recebe a notificação do servidor (e.g., chamada de paciente) e envia aos clientes
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Envia a mensagem para o grupo de notificação
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Recebe a mensagem do grupo e a envia para o WebSocket
    async def chat_message(self, event):
        message = event['message']

        # Envia a mensagem para o WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
