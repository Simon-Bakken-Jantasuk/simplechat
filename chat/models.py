from django.conf import settings
from django.db import models

class Message(models.Model):
    thread_name = models.CharField(max_length=50)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField()
    created = models.DateTimeField()
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'From {self.sender.username} to {self.receiver.username} in {self.thread_name}'
