export const onlineSocket = new WebSocket(
  'ws://' +
    window.location.host +
    '/ws/chat/' +
    'online'    +
    '/'   
);
