from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model





User = get_user_model()


# Create your models here.
class ChatRoom (models.Model):
  name = models.CharField(max_length=100)
  users = models.ManyToManyField(User, related_name='chatrooms', blank="False")
  # usernames = PrimaryKeyRelatedField(queryset=User.objects.all())



  def __str__(self):
    return f"Room name: {self.name}, Room ID: {self.id}"
