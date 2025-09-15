from django.shortcuts import render
from .serializers import UserSerializer,UserProfileSerializer
from .models import User,UserProfile
from rest_framework import generics
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema

User = get_user_model()

@extend_schema(
    tags=['User-Registration'],
    description='User registration here'
)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@extend_schema(
    tags=['User'],
)
class LoginProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user.profile
