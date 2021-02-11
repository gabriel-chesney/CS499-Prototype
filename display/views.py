from django.shortcuts import render
from display.models import *
from datetime import date
from django.db.models import Count, Min, Subquery

# Create your views here.
def display(request):
    rooms = Room.objects.all()
    
    events_distinct = Event.objects.filter(date=date.today()).order_by('-timeStart').values('room').distinct().annotate(occurrences=Count('room'), pk=Min('pk'))
    events = Event.objects.filter(id__in=Subquery(events_distinct.values('pk')))
    context = {
        "rooms" : rooms,
        "events" : events,
    }
    return render(request, 'display.html', context)