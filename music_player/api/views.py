from django.shortcuts import render
from rest_framework import generics, serializers, status
from .serializers import RoomSerializer, CreateRoomSerializer
from .models import Room 
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# Write endpoint /hello, /hi 

#api view, view of list of different room 

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer
    def post(self, request, format=None):
        pass
