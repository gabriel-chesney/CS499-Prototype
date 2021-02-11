from django.db import models

# Create your models here.
class Room(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    def __str__(self):
        return self.id

class Event(models.Model):
    name = models.CharField(max_length=20)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    group = models.CharField(max_length=20)
    timeStart = models.TimeField(auto_now=False, auto_now_add=False)
    timeEnd = models.TimeField(auto_now=False, auto_now_add=False)
    date = models.DateField()