from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from .serializers import ClientSerializer
from .models import Client
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

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