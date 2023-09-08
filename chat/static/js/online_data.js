import { onlineSocket } from './online_websocket.js';

onlineSocket.onmessage = (e) => {
  const data = JSON.parse(e.data);

  const onlineStatus = document.querySelector('#onlineStatus');

  onlineStatus.innerHTML = '';

  for (const username in data.connected_clients) {
    const statusDiv = document.createElement('div');
    if (data.connected_clients[username]) {statusDiv.innerText = `${username} is online.`};
    onlineStatus.appendChild(statusDiv);
  };
};
