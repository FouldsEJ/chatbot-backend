# from django.shortcuts import render

from operator import truediv
from .models import Chat
from .serializers import ChatSerializer
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated



class ListView(APIView):
    def get(self, _request):
        chats = Chat.objects.all()
        
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)


class ChatView(RetrieveUpdateDestroyAPIView):
   permission_classes = [IsAuthenticated, ]
   def get(self, _request, pk):

    obj = list(Chat.objects.filter(ChatRoomID=pk))
    serializer_class = ChatSerializer(obj, many=True)

    return JsonResponse( {'data': serializer_class.data})

class SendChatView(APIView):
      permission_classes = [IsAuthenticated, ]
     
      def post(self, request, pk):
        serializer = ChatSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Chat sent'})

        return Response(serializer.errors, status=422)


# Create your views here.
