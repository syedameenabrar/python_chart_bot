// Function to append messages to the chatbox
function appendMessage(message, sender = 'chatbot') {
    const chatbox = document.getElementById('chatbox');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');
    if (sender === 'user') {
        messageElement.classList.add('user-message');
        messageElement.textContent = 'User: ' + message;
    } else {
        messageElement.classList.add('chatbot-message');
        messageElement.textContent = 'Chatbot: ' + message;
    }
    chatbox.appendChild(messageElement);
    chatbox.scrollTop = chatbox.scrollHeight;  // Scroll to the bottom
}

// Function to send the message and get the response
async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (!userInput) return;

    // Append the user message to the chatbox
    appendMessage(userInput, 'user');

    try {
        const response = await fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',  // Ensure this header is set correctly
            },
            body: JSON.stringify({ message: userInput })  // Send user input in JSON format
        });

        // Check if the response is successful
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        // Get the response data from the server
        const data = await response.json();

        // Display the bot's reply
        const botReply = data.response || 'Sorry, no reply from the chatbot.';
        appendMessage(botReply);
    } catch (error) {
        console.error('Error:', error);
        appendMessage('Error occurred: ' + error.message);
    }

    // Clear the input field
    document.getElementById('user-input').value = '';
}
