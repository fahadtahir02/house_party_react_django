# Create your models here.
from django.db import models
import string, random 






#Logic creating database of a room
#Room has a host which can invite other listeners to join the room 
#ONLY Host controls music




def code_generator():
    length = 4

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k = length))
        if Room.objects.filter(code = code).count() == 0:
            break

    return code

class Room(models.Model):
    #host id
    #room id
    #music
    code = models.CharField(max_length = 8, default = 0, unique = True)
    host = models.CharField(max_length = 50, unique = True)
    guest_can_pause = models.BooleanField(null=False, default = False)
    votes_to_skip = models.IntegerField(null = False, default = 1)
    created_at = models.DateField(auto_now_add = True)

