from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from .serializers import ClientSerializer, EventSerializer
from .models import Client, Event
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Min
import datetime

from django.contrib.auth.models import User, Group

# Create your views here.

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def ClientsView(request):
    if request.method == "GET":
        clients = Client.objects.filter(user_id=request.user.id)
        serializedClients = ClientSerializer(clients, many=True)
        return Response(serializedClients.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data.dict()
        data["user_id"] = request.user.id
        serializedClient = ClientSerializer(data=data)
        serializedClient.is_valid(raise_exception=True)
        serializedClient.save()
        return Response(serializedClient.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def SingleClientView(request, id):
    client = get_object_or_404(Client, pk=id)
    clientUserID = getattr(client, "user_id").id
    if clientUserID != request.user.id:
        return Response({"message": "You are not authorized."}, status=status.HTTP_403_FORBIDDEN)
    elif request.method == "GET":
        serializedClient = ClientSerializer(client)
        return Response(serializedClient.data)
    elif request.method == "DELETE":
        client.delete() 
        return Response({"message": "Client deleted."}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        data = request.data.dict()
        data["user_id"] = request.user.id
        serializedClient = ClientSerializer(client, data=data) 
        serializedClient.is_valid(raise_exception=True)
        serializedClient.save()
        return Response(serializedClient.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH":
        serializedClient = ClientSerializer(client, data=request.data, partial=True) 
        serializedClient.is_valid(raise_exception=True)
        serializedClient.save()
        return Response(serializedClient.data, status=status.HTTP_200_OK)
    
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def EventsView(request):
    if request.method == "GET":
        client_id = request.query_params.get('client')
        start_date = request.query_params.get("start")
        end_date = request.query_params.get("end")
        if not end_date:
            end_date = datetime.date.today().strftime('%Y-%m-%d')
        if not start_date:
            first_date = Event.objects.all().aggregate(Min('date'))
            start_date = (first_date['date__min'].strftime('%Y-%m-%d'))
        events = Event.objects.filter(user_id=request.user.id)
        if client_id:
            client = get_object_or_404(Client, pk=client_id)
            if client.user_id.id == request.user.id:
                print("hello")
                events = events.filter(client_id=client.id)
            else:
              return Response({"message": "You are not authorized."}, status=status.HTTP_403_FORBIDDEN)  
        events = events.filter(date__gte=start_date, date__lte=end_date)
        serializedEvents = EventSerializer(events, many=True)
        return Response(serializedEvents.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data.dict()
        data["user_id"] = request.user.id
        serializedEvent = EventSerializer(data=data)
        serializedEvent.is_valid(raise_exception=True)
        serializedEvent.save()
        return Response(serializedEvent.data, status=status.HTTP_201_CREATED)
    
@api_view(["GET", "PUT", "PATCH", "DELETE"])
@permission_classes([IsAuthenticated])
def SingleEventView(request, id):
    event = get_object_or_404(Event, pk=id)
    eventUserID = getattr(event, "user_id").id
    if eventUserID != request.user.id:
        return Response({"message": "You are not authorized."}, status=status.HTTP_403_FORBIDDEN)
    elif request.method == "GET":
        serializedEvent = EventSerializer(event)
        return Response(serializedEvent.data)
    elif request.method == "DELETE":
        event.delete() 
        return Response({"message": "Client deleted."}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        data = request.data.dict()
        data["user_id"] = request.user.id
        serializedEvent = EventSerializer(event, data=data) 
        serializedEvent.is_valid(raise_exception=True)
        serializedEvent.save()
        return Response(serializedEvent.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH":
        serializedEvent = EventSerializer(event, data=request.data, partial=True) 
        serializedEvent.is_valid(raise_exception=True)
        serializedEvent.save()
        return Response(serializedEvent.data, status=status.HTTP_200_OK)