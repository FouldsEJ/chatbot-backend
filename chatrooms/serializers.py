from rest_framework import serializers
from .models import ChatRoom
from jwt_auth.models import CustomUser
from jwt_auth.serializers import *


class ChatRoomSerializer (serializers.ModelSerializer):

   users = UserSerializerForChatrooms(many=True)
   class Meta:
    model = ChatRoom
    fields = ('__all__')


class ChatRoomSerializer2 (serializers.ModelSerializer):

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