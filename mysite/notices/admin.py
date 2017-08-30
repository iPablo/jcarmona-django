from django.contrib import admin
from .models import Notice, Event

# Register your models here.
"""class notices on admin panel"""
class NoticesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'publish_date')

"""class events on admin panel"""
class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')

admin.site.register(Notice, NoticesAdmin)
admin.site.register(Event, EventsAdmin)