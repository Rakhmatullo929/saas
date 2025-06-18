from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema


class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    @extend_schema(
        summary="User Registration",
        description="Register a new user account"
    )
    def post(self, request):
        """
        Register a new user
        """
        data = request.data
        
        if User.objects.filter(username=data.get('username')).exists():
            return Response({
                'error': 'Username already exists'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(email=data.get('email')).exists():
            return Response({
                'error': 'Email already exists'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password'),
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', '')
        )
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            },
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]
    
    @extend_schema(
        summary="User Login",
        description="Login with username and password"
    )
    def post(self, request):
        """
        Login user
        """
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                },
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            })
        
        return Response({
            'error': 'Invalid credentials'
        }, status=status.HTTP_401_UNAUTHORIZED)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    @extend_schema(
        summary="Get User Profile",
        description="Get current user profile information"
    )
    def get(self, request):
        """
        Get user profile
        """
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'date_joined': user.date_joined,
        })
