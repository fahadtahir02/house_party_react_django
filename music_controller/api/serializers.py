#Responsible for translating our model and python code and translate that model into a json response
from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room #our table name 
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at') #our table columns 


