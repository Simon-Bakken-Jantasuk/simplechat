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
    1. [DATETIME_FORMAT](#datetime)
4. [License](#license)

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

There is the `settings.py`, [templates](/chat/templates/chat) and [JS](/chat/static/js) you can customize. It is a matter of overriding the files you want to customize.

### DATETIME_FORMAT <a name="datetime"></a>

Go to settings, change or add the `DATETIME_FORMAT` variable to change the time. More information is here, [DATETIME_FORMAT](https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-DATETIME_FORMAT) and [DATE](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#std-templatefilter-date).

-----------------------

## License <a name="license"></a>

[MIT](LICENSE)

-----------------------

