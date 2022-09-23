from django.urls import path
from .views import *

urlpatterns = [
    path('allchats/', ListView.as_view()),
    path('<int:pk>/', ChatView.as_view()),
    path('<int:pk>/sendmessage', SendChatView.as_view())
]
