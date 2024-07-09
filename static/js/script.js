function addComment() {
    var commentText = document.getElementById("comment-text").value;

    if (commentText.trim() === "") {
        alert("Por favor, digite um comentário.");
        return;
    }

    var commentContainer = document.getElementById("comments-container");
    var commentElement = document.createElement("div");
    commentElement.textContent = commentText;
    commentContainer.appendChild(commentElement);

    // Limpar o campo de texto após adicionar o comentário
    document.getElementById("comment-text").value = "";
}