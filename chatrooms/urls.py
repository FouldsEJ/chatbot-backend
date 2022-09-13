from django.urls import path
from .views import *

urlpatterns = [
    path('', ListView.as_view()),
    path('<int:pk>/', ListView.as_view()),
    path('createchat/', CreateChatView.as_view())
]
