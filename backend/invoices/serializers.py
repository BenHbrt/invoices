from rest_framework import serializers
from .models import Client, Event

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("id", "name", "addressStreet", "addressLocality", "addressPostcode", "addressCity", "IC", "user_id")

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("id", "title", "client_id", "user_id", "date", "duration", "amount")