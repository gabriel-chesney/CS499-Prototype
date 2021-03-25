from django.contrib import admin
from display.models import Room, Event, Theme

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'room', 'date', 'timeStart')
    pass

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    list_editable = ('active',)
    pass

admin.site.register(Room, RoomAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.site_header = "Morehead State University SCES Digital Signage & Room Management"
admin.site.site_title = "SCES Administration"
admin.site.index_title = "SCES Administration"