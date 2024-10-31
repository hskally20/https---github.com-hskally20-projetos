
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