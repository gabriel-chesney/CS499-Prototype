from django.contrib import admin
from display.models import Room, Event

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Room, RoomAdmin)
admin.site.register(Event, EventAdmin)