# from django.shortcuts import render

from operator import truediv
from .models import Chat
from .serializers import ChatSerializer
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response


class ListView(APIView):
    def get(self, _request):
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)


class ChatView(RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
# Create your views here.
