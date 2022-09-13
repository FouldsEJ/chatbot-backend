from rest_framework import serializers
from .models import ChatRoom
from jwt_auth.models import CustomUser

class ChatRoomSerializer (serializers.ModelSerializer):
  class Meta:
    model = ChatRoom
    fields = ('__all__')

# class UserSerializer (serializers.ModelSerializer):
#   class Meta:
#     model = CustomUser
#     fields = ('__all__')

# class PopulatedChatroomSerializer(ChatRoomSerializer):
#   chatroom = ChatRoomSerializer()
#   users = UserSerializer(many=True)