from calendar import timegm
from time import time
from django.db import models
from jwt_auth.models import CustomUser
from chatrooms.models import ChatRoom


# Create your models here.


class Chat(models.Model):
    chat_id = models.AutoField(auto_created=True,
                               primary_key=True,
                               serialize=False,
                               verbose_name='ID'
                               )
    sender_id = models.ForeignKey(
        CustomUser, related_name='chat_userID', default=None, on_delete=models.CASCADE, blank='True')
    creation_time = models.DateTimeField(auto_now_add=True)
    message = models.TextField(unique=False)
    messageDelivered = models.BooleanField(default=False)
    messageRead = models.BooleanField(default=False)
    ChatRoomID = models.ForeignKey(
        ChatRoom, related_name='chatroom_chat', default=None, on_delete=models.CASCADE, blank=True, )


def __str__(self):
    return self.chat_id
