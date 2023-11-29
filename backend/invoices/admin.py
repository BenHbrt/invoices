from django.contrib import admin
from .models import Client, Event

class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "addressStreet", "addressLocality", "addressPostcode", "addressCity", "IC")

class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "client_id", "user_id", "date", "duration", "amount")

# Register your models here.

admin.site.register(Client, ClientAdmin)
admin.site.register(Event, EventAdmin)