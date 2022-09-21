from django.urls import path 
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('credentials/', CredentialsView.as_view()),
    path('allusers/<int:pk>/', ListViewUserFromId.as_view()),
    path('allusers/', ListViewForAllUsers.as_view()),
]