from django.contrib import admin

# Register your models here.

from .models import Environment, Host, Context

admin.site.register(Environment)
admin.site.register(Host)
admin.site.register(Context)
