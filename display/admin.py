from django.contrib import admin
from display.models import Room, Event, Theme


# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        fields = list(super().get_readonly_fields(request))
        if not request.user.is_superuser:
            fields.append('approved', 'author')
        fields.append('author')
        return fields

    def has_change_permission(self, request, obj=None):
        if obj is not None and request.user.is_superuser:
            return True
        elif obj is not None and obj.author != request.user:
            return False
        return True
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set author during the first save.
            obj.author = request.user
        super().save_model(request, obj, form, change)

    list_display = ('name', 'group', 'room', 'date', 'timeStart', 'approved')
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