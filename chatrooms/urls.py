from django.urls import path
from .views import *

urlpatterns = [
    path('', ListView.as_view()),
    path('<int:pk>/', ChatRoomDetail.as_view()),
    path('allchatrooms/<int:pk>/', ListAllChatsView.as_view()),
    path('createchat/', CreateChatView.as_view())
]
