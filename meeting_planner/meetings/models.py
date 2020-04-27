from django.db import models
from datetime import time


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField(default=1)
    room_number = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.room_number} - {self.name} | Floor {self.floor}"


class Meeting(models.Model):
    title=models.CharField(max_length=200)
    date = models.DateField()
    starttime =models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.starttime} on {self.date} | Floor: {self.room.floor} Room: {self.room.name}"

        # | {self.room.name}- Floor {self.room.floor} "


