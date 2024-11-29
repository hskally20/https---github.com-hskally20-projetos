
document.querySelectorAll('.chamar-paciente').forEach(function(button) {
    button.addEventListener('click', function() {
        const pacienteId = this.getAttribute('data-paciente-id');  // Obtém o ID do paciente
        const csrftoken = this.getAttribute('data-csrf');  // Obtém o CSRF token
    
        // Envia o pedido AJAX para chamar o paciente
        fetch("{% url 'chamar-paciente' %}", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
            "X-Requested-With": "XMLHttpRequest"  // Verifique se este cabeçalho está sendo realmente enviado
        },
        body: JSON.stringify({ paciente_id: pacienteId })
    })
    
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Notificação enviada com sucesso!');
                document.getElementById('mensagem').textContent = data.message;
            } else {
                alert('Erro: ' + data.message);
            }
        });
    });
});
document.addEventListener('DOMContentLoaded', function() {
    // Adicionando um único event listener para toda a tabela
    const table = document.querySelector('.table'); // Seleciona a tabela

    table.addEventListener('click', function(event) {
        // Verifica se o clique foi em um botão de "marcar como lida"
        if (event.target && event.target.classList.contains('btn-success')) {
            const id = event.target.getAttribute('data-id');
            marcarComoLida(id);
        }
    });

    function marcarComoLida(id) {
        // Mudar a cor da linha para indicar que foi lida
        const row = document.getElementById("notificacao_" + id);
        row.style.backgroundColor = "#d3ffd3"; // Cor de fundo para 'lida'

        // Atualizar o status no campo da tabela
        const status = document.getElementById("status_" + id);
        status.textContent = "Lida";

        // Aqui você pode adicionar um AJAX ou redirecionamento para atualizar o status no banco
        // Exemplo: enviar uma requisição para o Django para alterar o status da notificação
    }
});
