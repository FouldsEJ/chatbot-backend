from django.urls import path
from .views import *

urlpatterns = [
    path('chatrooms/', ListView.as_view())
]
