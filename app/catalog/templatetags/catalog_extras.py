from django import template
from catalog.models import Version

register = template.Library()

@register.simple_tag
def get_latest_version(app_name):
    try:
    	version_string = Version.objects.filter(app=app_name).values("version").latest('created').get("version")
    except Version.DoesNotExist:
    	version_string = ''
    return version_string

@register.simple_tag
def get_latest_version_date(app_name):
    try:
        time = Version.objects.filter(app=app_name).order_by('-created').first()
    except Exception:
    	time = ''
    return time