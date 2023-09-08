from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.conf import settings
from .models import Message 

User = get_user_model()

from django.views.decorators.cache import never_cache
@never_cache
@login_required()
def index(request):
    users = User.objects.exclude(username=request.user.username)
    context = {'users': users}
    return render(request, 'chat/index.html', context)

@never_cache
@login_required()
def room(request, username):
    sender = get_object_or_404(User, username=request.user.username)
    receiver = get_object_or_404(User, username=username)

    if request.user.id > receiver.id:
        thread_name = f'chat_{request.user.id}-{receiver.id}'
    else:
        thread_name = f'chat_{receiver.id}-{request.user.id}'

    messages = Message.objects.filter(thread_name=thread_name)

    context = {
        'sender': sender,
        'receiver': receiver,
        'messages': messages,
        'datetime_format': settings.DATETIME_FORMAT,
    }
    
    return render(request, 'chat/room.html', context)
