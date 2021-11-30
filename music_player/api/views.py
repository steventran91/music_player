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
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            guest_can_pause = serializers.data.get('guest_can_pause')
            votes_to_skip = serializers.data.get('votes_to_skip')
            host = self.request.session.session_key
            queryset = Room.objects.filter(host=host)
            if queryset.exist():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
            else:
                room = Room(host=host, guest_can_pause=guest_can_pause, votes_to_skip=votes_to_skip)
                room.save()

            return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)


