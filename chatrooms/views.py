from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView


from chatrooms.models import ChatRoom
from chatrooms.serializers import ChatRoomSerializer
from rest_framework.response import Response

# Create your views here.

class ListView(ListCreateAPIView):
  # def get(self, request):
  #   chatrooms = ChatRoom.objects.all()
  #   serialzer = ChatRoomSerializer(chatrooms, many=True)
  #   return Response(serialzer.data)
  queryset = ChatRoom.objects.all()
  serializer_class = ChatRoomSerializer


class ChatRoomDetail(RetrieveUpdateDestroyAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

