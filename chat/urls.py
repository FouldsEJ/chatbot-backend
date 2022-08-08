from django.urls import path
from .views import *

urlpatterns = [
    path('chats/', ListView.as_view()),
    path('<int:pk>/', ChatView.as_view())
]
