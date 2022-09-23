from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django.views.generic.detail import DetailView
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

from chatrooms.models import ChatRoom
from chatrooms.serializers import *
from rest_framework.response import Response

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

class ListView(DetailView):
   permission_classes = [IsAuthenticated, ]
   def get(self, request, pk):
    chatroom = ChatRoom.objects.get(id=pk)
         
    if not chatroom.users.filter(self.request.user): # Or how ever you validate
     raise PermissionDenied('User is not allowed to modify listing')
    
     serializer = ChatRoomSerializer(chatroom)
     serializer2 = UserSerlializer(chatroom.users)
     return Response(serializer.data,)


class ListAllChatsView(APIView):
   permission_classes = [IsAuthenticated, ]
   def get(self, _request, pk):
        
      obj = list(ChatRoom.objects.filter(users=pk))
      serializer_class = ChatRoomSerializer(obj, many=True)
        
      return JsonResponse( {'data': serializer_class.data})

      
  
class CreateChatView(APIView):
      permission_classes = [IsAuthenticated, ]
     
      def post(self, request):
        serializer = ChatRoomSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Chatroom created', 'chatroomId': serializer.data})

        return Response(serializer.errors, status=422)

class ChatRoomDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, ]
    
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer


    

    

    

