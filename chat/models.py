from calendar import timegm
from time import time
from django.db import models

# Create your models here.


class chat(models.Model):
    chat_id = models.AutoField(auto_created=True,
                               primary_key=True,
                               serialize=False,
                               verbose_name='ID'
                               )
    # sender_id = models.ForeignKey(UserID,)
    creation_time = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length='', unique=False)
    messageDelivered = models.BooleanField(default=False)
    messageRead = models.BooleanField(default=False)
    # ChatRoomID = models.ForeignKey(CharRoomID,)


def __str__(self):
    return self.chat_id
