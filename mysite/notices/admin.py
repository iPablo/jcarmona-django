from django.contrib import admin
from .models import Notice, Event

# Register your models here.
class NoticesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'publish_date')

class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')

admin.site.register(Notice, NoticesAdmin)
admin.site.register(Event, EventsAdmin)