from rest_framework import serializers
from .models import Chat
from jwt_auth.serializers import UserSerializerForChatrooms


class ChatSerializer(serializers.ModelSerializer):
    sender_id = UserSerializerForChatrooms()
    class Meta:
        model = Chat
        fields = '__all__'


class ChatSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'