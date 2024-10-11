const express = require('express');
const WebSocket = require('ws');
const path = require('path');

const app = express();
const server = require('http').createServer(app);
const wss = new WebSocket.Server({ server });

app.use(express.static(path.join(__dirname, 'static')));

// server.js
const express = require('express');
const WebSocket = require('ws');

const app = express();
const server = require('http').createServer(app);
const wss = new WebSocket.Server({ server });

let pacientes = [];
let usuarios = {}; // { usuarioId: socket }

wss.on('connection', (ws) => {
    ws.on('message', (message) => {
        const data = JSON.parse(message);
        
        if (data.type === 'register') {
            usuarios[data.usuarioId] = ws;
        } else if (data.type === 'cadastrarPaciente') {
            pacientes.push(data.paciente);
        } else if (data.type === 'chamarPaciente') {
            const paciente = pacientes.find(p => p.id === data.pacienteId);
            if (paciente && usuarios[paciente.cadastradorId]) {
                usuarios[paciente.cadastradorId].send(JSON.stringify({ type: 'notificacao', message: `Paciente ${paciente.nome} foi chamado!` }));
            }
        }
    });
});

server.listen(3000, () => {
    console.log('Servidor rodando na porta 8000');
});

