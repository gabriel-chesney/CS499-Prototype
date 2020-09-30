from django.shortcuts import render
from display.models import *
from datetime import date

# Create your views here.
def display(request):
    rooms = Room.objects.all()
    events = Event.objects.filter(date=date.today()).values('room').distinct().order_by('room', 'timeStart')
    context = {
        "rooms" : rooms,
        "events" : events,
    }
    return render(request, 'display.html', context)