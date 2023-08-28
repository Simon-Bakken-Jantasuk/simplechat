import { messageSocket, typingSocket } from './websocket.js';

/**
 * Event handler for the typingSocket's 'message' event.
 * Updates the typing indicator based on incoming messages.
 * @param {MessageEvent} e - The WebSocket message event.
 */
typingSocket.onmessage = (e) => {
  const data = JSON.parse(e.data);
  if (data.typing) {
    typingIndicator.textContent = `${data.sender_username} is typing...`;
  } else {
    typingIndicator.textContent = '';
  };
};

/**
 * Event handler for the messageSocket's 'message' event.
 * Appends incoming chat messages to the chat log.
 * @param {MessageEvent} e - The WebSocket message event.
 */
messageSocket.onmessage = (e) => {
  const data = JSON.parse(e.data);
  const chatLog = document.getElementById('chat-log');
  const messageDiv = document.createElement('div');
  messageDiv.textContent = `${data.sender_username}: ${data.message} | ${data.datetime_format}`;
  chatLog.appendChild(messageDiv);
};
