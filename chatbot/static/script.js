function sendMessage() {
    const inputField = document.getElementById('user-input');
    const message = inputField.value.trim();
    if (message === '') return;

    const chatBox = document.getElementById('chat-box');

    // 1. பயனர் மெசேஜை திரையில் காட்டு
    const userDiv = document.createElement('div');
    userDiv.className = 'user-msg';
    userDiv.innerText = message;
    chatBox.appendChild(userDiv);

    inputField.value = '';
    chatBox.scrollTop = chatBox.scrollHeight;

    // 2. Django Backend-க்கு மெசேஜை அனுப்பு
    fetch('/get-response/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        // 3. பாட் பதிலைத் திரையில் காட்டு
        const botDiv = document.createElement('div');
        botDiv.className = 'bot-msg';
        botDiv.innerText = data.reply;
        chatBox.appendChild(botDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => console.error('Error:', error));
}