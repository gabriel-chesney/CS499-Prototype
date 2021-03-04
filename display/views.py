from django.shortcuts import render
from display.models import *
from datetime import date, datetime
from django.db.models import Count, Min, Subquery, Max

# Create your views here.
def display(request):
    rooms = Room.objects.all()
    
    events = Event.objects.filter(date=date.today()).order_by('room').order_by('timeStart')

    context = {
        "rooms" : rooms,
        "events" : events,
    }
    return render(request, 'display.html', context)