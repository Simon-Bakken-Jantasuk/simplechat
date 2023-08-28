<div align="center">
    <h1>SimpleChat</h2>
    <img src="simplechat.gif">
</div>

----------

# Table of contents
1. [Introduction](#introduction)
   1. [What problem was solved?](#introduction1)
   2. [Installation](#introduction2)
   3. [Quick Start](#introduction3)
   4. [Features](#introduction4)

3. [Documentation](#docs)
    1. [How do I change the time format for messages?](#datetime)
4. [Goals](#goals)
5. [License](#license)

## Introduction <a name="introduction"></a>

SimpleChat is created with Channels, WebSockets, and Javascript as frontend. 
The project is inspired by the django-allauth battery-loaded authentication system.
The initial idea is to create a simple way to add chatting functionality to any Django project.
The project's core idea is for it to be as simple as possible, hence the name simplechat. 

### What problem was solved? <a name="introduction1"></a>
There is no library which allows easy addition for chatting system for Django.
If you are interested in customizablity, battery loaded chatting system, which is free and open source, then SimpleChat is for you.

### Installation <a name="introduction2"></a>

#### Installation with PIP

```shell
pip install django-simplechat
```

#### Build the package 

##### Download the repository

```shell
git clone https://github.com/Simon-Bakken-Jantasuk/simplechat/
```

##### Build

```shell
cd simplechat/build/
chmod +x build.sh
./build.sh
cd django-simplechat
python setup.py sdist
```

### Quick start <a name="introduction3"></a>

##### After installation [Quick start for SimpleChat](/build/django-simplechat/README.md)

### Features <a name="introduction4"></a>

1. Private chat (branch: master)
2. Customizable datetime (branch: master)
3. Customizable message (branch: master)
4. Typing Indicator (branch: feat-typing)

-----------------------

## Documentation <a name="docs"></a>

### How to change the time format for messages? <a name="datetime"></a>

Go to settings, change or add the `DATETIME_FORMAT` variable to change the time. More information is here, [DATETIME_FORMAT](https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-DATETIME_FORMAT) and [DATE](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#std-templatefilter-date).

### How to typingIndicator or message? <a name="data.js"></a>

Create a [data.js](/chat/static/js/data.js) in your static directory in a folder named chat.

```js
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
```

There is two multiple WebSockets– messageSocket which contains the sender username, the message and some information about the time. The typingSocket contains simply the sender and typing which has either a boolean true or false. You can also override templates aswell, the [room.html](/chat/templates/chat/room.html) and so on. For more information: [templates](/chat/templates/chat) and [js](/chat/static/js)

## Goals <a name="goals"></a>

- [ ] Turn simplechat to an API
- [ ] Online status functionality
- [ ] Anonymous chatting with users
- [ ] Notification indicator 
- [ ] Spam protection

## License <a name="license"></a>

[MIT](LICENSE)

