fetch("{% url 'listar_paciente' %}", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken
    },
    body: JSON.stringify({ paciente_id: pacienteId })
})

