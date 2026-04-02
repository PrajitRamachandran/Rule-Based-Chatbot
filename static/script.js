const inputField = document.getElementById("user-input");

// Listen for Enter key to submit
inputField.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});

async function sendMessage() {
    let input = document.getElementById("user-input");
    let message = input.value.trim();
    
    if (message === "") return; // Prevent empty messages

    let chatBox = document.getElementById("chat-box");

    // Render User Message
    let userMsgHTML = `<div class="message user-message slide-in">${message}</div>`;
    chatBox.insertAdjacentHTML("beforeend", userMsgHTML);

    input.value = "";
    scrollToBottom();

    // Show a temporary "Processing..." indicator for realism
    let typingID = "typing-" + Date.now();
    let typingHTML = `<div id="${typingID}" class="message bot-message slide-in" style="opacity: 0.6; font-style: italic;">Processing...</div>`;
    chatBox.insertAdjacentHTML("beforeend", typingHTML);
    scrollToBottom();

    try {
        let response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        let data = await response.json();

        // Remove the processing indicator
        document.getElementById(typingID).remove();

        // Render Bot Message
        let botMsgHTML = `<div class="message bot-message slide-in">${data.response}</div>`;
        chatBox.insertAdjacentHTML("beforeend", botMsgHTML);
        
        scrollToBottom();
    } catch (error) {
        document.getElementById(typingID).remove();
        let errorMsgHTML = `<div class="message bot-message slide-in" style="color: #ef4444;">Network error. Cannot reach backend.</div>`;
        chatBox.insertAdjacentHTML("beforeend", errorMsgHTML);
    }
}

function scrollToBottom() {
    let chatBox = document.getElementById("chat-box");
    chatBox.scrollTop = chatBox.scrollHeight;
}