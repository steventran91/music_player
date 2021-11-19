from django.shortcuts import render
from rest_framework import generics, serializers
from .serializers import RoomSerializer
from .models import Room 

# Create your views here.
# Write endpoint /hello, /hi 

#api view, view of list of different room 

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
