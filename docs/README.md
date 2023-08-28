<div class="center">
    <h2 class="title">SimpleChat</h2>
    <img src="simplechat.gif">
</div>

<style>
.center{
    display: flex;
    justify-content: center;
}
</style>

----------

#### What problem was solved?

Project was inspired by django-allauth battery loaded authentication system.
The initial idea is to create a simple way to add chatting functionality to any Django project.
The project core idea is for it to be as simple as possible, hence the name simplechat. 
It is supposed to be customizable, and battery loaded.

----------

#### Technology 

1. Django Channels, with WebSockets
2. Django 
3. Plain Javascript

----------

#### Features

Typing Indicator (branch: feat-typing)

----------

#### License 

[MIT](LICENSE)

----------

#### Goals

- [x] Private chat
- [x] Customizable datetime for private chat 
- [x] Customizable message for private chat 
- [ ] Turn simplechat to an API
- [ ] Online status functionality
- [ ] Anonymous chatting with users
- [ ] Notification indicator 
- [ ] Spam protection 
