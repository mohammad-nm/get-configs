"use strict";
//fetching messages
async function fetchMessages() {
  try {
    const response = await fetch("YOUR API");
    const messages = await response.json();
    displayMessages(messages);
  } catch (error) {
    console.error("Error fetching messages:", error);
  }
}
//show configs in the element with "message" id
function displayMessages(messages) {
  const messagesDiv = document.getElementById("messages");
  messagesDiv.innerHTML = messages;
}

fetchMessages();

//refreash eevery 5 second
setInterval(fetchMessages, 5000);
