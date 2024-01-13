from .models import Room 
from .serializers import RoomSerializer
from django.shortcuts import render
from rest_framework import generics # allow us to create a class that inherits from a generic api view



#Here is where all endpoints go


# def main(request):
#     return HttpResponse("Hello")



##Creating api view


class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer