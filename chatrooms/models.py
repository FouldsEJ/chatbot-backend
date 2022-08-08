from django.db import models

# Create your models here.
class ChatRoom (models.Model):
  name = models.CharField(max_length=100)
  image = models.CharField(max_length=100)
  # users = models.ManyToManyField(User, related_name='chatrooms')


  def __str__(self):
    return self.name