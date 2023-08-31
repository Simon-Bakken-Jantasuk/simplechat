export const receiver_id = JSON.parse(document.getElementById('receiver_id').textContent);
export const sender_username = JSON.parse(document.getElementById('sender_username').textContent);
export const receiver_username = JSON.parse(document.getElementById('receiver_username').textContent);

export const chatSocket = new WebSocket(
  'ws://'
    + window.location.host
    + '/ws/chat/'
    + receiver_id
    + '/'
);

document.querySelector('#chat-form').onsubmit = (e) => {
  e.preventDefault(); 
  const messageInputDom = document.querySelector('#chat-message-input');
  const message = messageInputDom.value;
  chatSocket.send(JSON.stringify({
    'message': message,
    'sender_username': sender_username,
    'receiver_username': receiver_username,
  }));
  messageInputDom.value = '';
};
