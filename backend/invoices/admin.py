from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "addressStreet", "addressLocality", "addressPostcode", "addressCity", "IC")

# Register your models here.

admin.site.register(Client, ClientAdmin)