from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView

from chatrooms.models import ChatRoom
from chatrooms.serializers import ChatRoomSerializer
from rest_framework.response import Response

# Create your views here.

class ListView(APIView):
  def get(self, request):
    chatrooms = ChatRoom.objects.all()
    serialzer = ChatRoomSerializer(chatrooms, many=True)
    return Response(serialzer.data)