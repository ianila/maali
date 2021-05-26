from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import response, status
from django.contrib.auth import authenticate
from rest_framework import permissions

from .models import MaaliUser
from .serializers import RegisterSerializer, LoginSerializer, UserDetailsSerializer

class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_409_CONFLICT)

class LoginView(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        
        return response.Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserDetailView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, email):
        try:
            return MaaliUser.objects.get(email=email)
        except MaaliUser.DoesNotExist:
            return response.Response({'error': 'No user found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        email = request.data.get('email', None)
        user = self.get_object(email)
        serializer = UserDetailsSerializer(user)
        return response.Response(serializer.data)