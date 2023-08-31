import { chatSocket } from './base_chat.js';

chatSocket.onmessage = (e) => {
  const data = JSON.parse(e.data)
  const chatLog = document.getElementById('chat-log');
  const messageDiv = document.createElement('div');
  messageDiv.textContent = `${data.sender_username}: ${data.message} | ${data.datetime_format}`;
  chatLog.appendChild(messageDiv);
};
