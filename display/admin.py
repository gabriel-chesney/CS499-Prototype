from django.contrib import admin
from display.models import Room, Event

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'room', 'date', 'timeStart')
    pass

admin.site.register(Room, RoomAdmin)
admin.site.register(Event, EventAdmin)
admin.site.site_header = "Morehead State University SCES Digital Signage & Room Management"