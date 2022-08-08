from django.urls import path 
from .views import CredentialsView, RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('credentials/', CredentialsView.as_view()),
]