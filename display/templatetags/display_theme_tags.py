import django
from django import template
from django.conf import settings
from django.urls import NoReverseMatch, reverse
from django.utils import translation

from display.models import Theme

register = template.Library()
simple_tag = register.simple_tag

@simple_tag(takes_context=True)
def get_display_theme(context):
    theme = Theme.get_active_theme()
    return theme