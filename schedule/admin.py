from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "date")
    readonly_fields = ('created_time',)


admin.site.register(Event, EventAdmin)
