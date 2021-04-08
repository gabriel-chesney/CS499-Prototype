from colorfield.fields import ColorField
from django.db import models
from django.db.models.signals import post_delete, post_save, pre_save
from admin_interface.cache import del_cached_active_theme
from django.utils.encoding import force_str
from django.contrib.auth.models import User
from django.conf import settings
from recurrence.fields import RecurrenceField

# Create your models here.
class Room(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    def __str__(self):
        return self.id

class Event(models.Model):
    name = models.CharField(max_length=20)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    group = models.CharField(max_length=20)
    timeStart = models.TimeField(auto_now=False, auto_now_add=False)
    timeEnd = models.TimeField(auto_now=False, auto_now_add=False)
    date = models.DateField()
    recDate = RecurrenceField(null = True)
    approved = models.BooleanField(default = False, verbose_name='approved')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

class Theme(models.Model):
    #Static Methods provided from django-admin-interface by fabiocaccamo
    @staticmethod
    def post_migrate_handler(**kwargs):
        del_cached_active_theme()
        Theme.get_active_theme()

    @staticmethod
    def post_delete_handler(**kwargs):
        del_cached_active_theme()
        Theme.get_active_theme()

    @staticmethod
    def post_save_handler(instance, **kwargs):
        del_cached_active_theme()
        if instance.active:
            Theme.objects.exclude(pk=instance.pk).update(active=False)
        Theme.get_active_theme()

    @staticmethod
    def pre_save_handler(instance, **kwargs):
        if instance.pk is None:
            try:
                obj = Theme.objects.get(name=instance.name)
                if obj:
                    instance.pk = obj.pk
            except Theme.DoesNotExist:
                pass

    @staticmethod
    def get_active_theme():
        objs_manager = Theme.objects
        objs_active_qs = objs_manager.filter(active=True)
        objs_active_ls = list(objs_active_qs)
        objs_active_count = len(objs_active_ls)

        if objs_active_count == 0:
            obj = objs_manager.all().first()
            if obj:
                obj.set_active()
            else:
                obj = objs_manager.create()

        elif objs_active_count == 1:
            obj = objs_active_ls[0]

        elif objs_active_count > 1:
            obj = objs_active_ls[-1]
            obj.set_active()

        return obj

    active = models.BooleanField(default = True, verbose_name='active')
    name = models.CharField(max_length=20)
    Page_Title = models.CharField(max_length = 30, default = "Title")
    Page_Header = models.CharField(max_length = 30, default = "Header")
    Page_Subheader_Top = models.CharField(max_length = 40, default = "Subheader: Top")
    Page_Subheader_Bottom = models.CharField(max_length = 40, default = "Subheader: Bottom")
    Background_Color = ColorField(default = '#FFFFFF')
    Font_Color = ColorField(default = '#000000')
    Table_Header_Row_Color = ColorField(default = '#FFFFFF')
    Table_Row_Color = ColorField(default = '#FFFFFF')
    Table_Row_Alt_Color = ColorField(default = '#FFFFFF')
    Table_Border_Color = ColorField(default = '#000000')

    def set_active(self):
        self.active = True
        self.save()
    
    def __str__(self):
        return force_str(self.name)
    
post_delete.connect(Theme.post_delete_handler, sender=Theme)
post_save.connect(Theme.post_save_handler, sender=Theme)
pre_save.connect(Theme.pre_save_handler, sender=Theme)