from django.urls import path, include
from django.contrib import admin
from display import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.display, name = 'display'),
    path(r"admin/", admin.site.urls, name="admin"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)