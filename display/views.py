from django.shortcuts import render
from display.models import Room, Event
from datetime import date, datetime
from django.db.models import Count, Min, Subquery, Max

# Create your views here.
def display(request):
    rooms = Room.objects.all().order_by("id")
    
    events = Event.objects.filter(date=date.today()).order_by('timeStart').order_by('room')

    context = {
        "rooms" : rooms,
        "events" : events,
    }
    return render(request, 'display.html', context)