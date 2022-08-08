from django.contrib.auth import get_user_model
from jwt_auth.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django.conf import settings
import jwt
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timedelta




User = get_user_model()

class RegisterView(APIView):
  def post(self, request):

    email = request.data.get('email')

    try: 
      User.objects.get(email=email)
      return Response({'message': 'A user with that email address already exists'})
    except User.DoesNotExist:
      pass

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': 'Registration successful'})
    
    return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class LoginView(APIView):
  def post(self, request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
      user = User.objects.get(email=email)
    except User.DoesNotExist:
      raise PermissionDenied({'message': 'Invalid credentials'})
    
    if not user.check_password(password):
      raise PermissionDenied({'message': 'Invalid credentials'})

    dt = datetime.now() + timedelta(days=1)  


    token = jwt.encode({'sub': user.id, 'username': user.username, 'exp': int(dt.strftime('%s'))}, settings.SECRET_KEY, algorithm='HS256')
    return Response({'token': token, 'message': f'Welcome back {user.username}!'})


class CredentialsView(APIView):

    permission_classes = [IsAuthenticated,]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)