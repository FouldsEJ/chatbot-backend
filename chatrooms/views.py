from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django.views.generic.detail import DetailView
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from chatrooms.models import ChatRoom
from chatrooms.serializers import ChatRoomSerializer
from rest_framework.response import Response

# Create your views here.

class ListView(DetailView):
  def get(self, request, pk):
    print('working')
    print(self)
    print(pk)
     
    chatroom = ChatRoom.objects.get(id=pk)
    print(chatroom)
    print(self.request)
    if not chatroom.users.filter(self.request.user): # Or how ever you validate
        raise PermissionDenied('User is not allowed to modify listing')

    serializer = ChatRoomSerializer(chatroom)
    return Response(serializer.data)
  
class CreateChatView(APIView):
      permission_classes = [IsAuthenticated, ]
     
      def post(self, request):
        serializer = ChatRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Chatroom created', 'chatroomId': serializer.data})

        return Response(serializer.errors, status=422)

class ChatRoomDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

