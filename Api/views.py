from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Tour
from .serializers import TourSerializer, UserSerializer, AgentSerializer
#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated, AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AgentViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AgentSerializer

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

















