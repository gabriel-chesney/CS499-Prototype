from django.shortcuts import render
from display.models import *
from datetime import date

# Create your views here.
def display(request):
    rooms = Room.objects.all()
    #events = Event.objects.raw('SELECT * FROM display_event WHERE room IN (SELECT max(room) FROM display_event GROUP BY name)')
    #events = Event.objects.all().order_by().values("room").distinct()
    events = Event.objects.all()
    context = {
        "rooms" : rooms,
        "events" : events,
    }
    return render(request, 'display.html', context)