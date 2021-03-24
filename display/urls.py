from django.urls import path
from display import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.display, name = 'display')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)