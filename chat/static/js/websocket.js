import { TYPING_TIMEOUT } from './settings.js';

export const inputField = document.querySelector('#chat-message-input');
export const typingIndicator = document.querySelector('#typingIndicator');

export const receiver_id = JSON.parse(document.getElementById('receiver_id').textContent);
export const sender_username = JSON.parse(document.getElementById('sender_username').textContent);
export const receiver_username = JSON.parse(document.getElementById('receiver_username').textContent);

/**
 * The current typing state ('idle' or 'typing').
 * @type {string}
 */
let typingState = 'idle';

/**
 * Timer used to track typing activity.
 * @type {number}
 */
let typingTimer;

export const messageSocket = new WebSocket(
  'ws://' +
    window.location.host +
    '/ws/chat/' +
    receiver_id +
    '/'
);

export const typingSocket = new WebSocket(
  'ws://' +
    window.location.host +
    '/ws/chat/' +
    receiver_id +
    '/typing/' 
);

document.querySelector('#chat-form').onsubmit = (e) => {
  e.preventDefault();
  const message = inputField.value;
  messageSocket.send(JSON.stringify({
    'sender_username': sender_username,
    'receiver_username': receiver_username,
    'message': message,
  }));
  inputField.value = '';
};

/**
 * Handles keydown events in the input field to track typing activity.
 * @param {KeyboardEvent} e - The keyboard event.
 */
inputField.onkeydown = (e) => {
  if (typingState === 'idle') {
    typingSocket.send(JSON.stringify({
      'sender_username': sender_username,
      'typing': true,
    }));
    typingState = 'typing';
  }
};

/**
 * Stops tracking typing activity when the user stops typing.
 */
const stopTyping = () => {
  if (typingState === 'typing') {
    typingSocket.send(JSON.stringify({
      'sender_username': sender_username,
      'typing': false,
    }));
    typingState = 'idle';
  }
};

/**
 * Handles input events in the input field to stop tracking typing activity after a timeout.
 */
inputField.oninput = () => {
  clearTimeout(typingTimer);
  typingTimer = setTimeout(() => {
    stopTyping();
  }, TYPING_TIMEOUT);
};
