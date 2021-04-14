from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from display.models import Room, Event, Theme, Group, xtendUser


# Register your models here.
class xtendUserInline(admin.StackedInline):
    model = xtendUser
    can_delete = False
    verbose_name = 'Group'

class UserAdmin(BaseUserAdmin):
    inlines = (xtendUserInline,)

class RoomAdmin(admin.ModelAdmin):
    pass

class GroupAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        fields = list(super().get_readonly_fields(request))
        if not request.user.is_superuser:
            fields.append('approved')
            fields.append('group')

        fields.append('author')
        fields.append('date')
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
            #obj.group = request.user.xtendUser.group
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
admin.site.register(Group, GroupAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)