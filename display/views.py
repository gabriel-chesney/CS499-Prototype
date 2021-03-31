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


#login stuff
def login(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('admin:index')
        else:
            return redirect('user_dashboard')
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = auth.authenticate(request,username=username,password=password)

            if user is not None:
                if user.is_staff:
                    auth.login(request,user)
                    return redirect('admin:index')
                else:
                    auth.login(request,user)
                    return redirect('user_dashboard')
            else:
                messages.info(request,"Username or Password is incorrect")
                return redirect('login')

