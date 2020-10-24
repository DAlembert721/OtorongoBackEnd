from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop_system.serializers import *


# Create your views here.

@api_view(['GET'])
def rates_list(request):
    if request.method == 'GET':
        rates = Rate.objects.all()
        serializer = RateSerializer(rates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST', 'GET'])
def account_clients_list(request, account_id):
    try:
        Account.objects.get(id=account_id)
    except Account.DoesNotExist:
        return Http404

    if request.method == 'GET':
        clients = Client.objects.filter(account__id=account_id)
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(account_id=account_id, rate_id=request.data["rate_id"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def account_clients_detail(request, account_id, client_id):
    try:
        Account.objects.get(id=account_id)
    except Account.DoesNotExist:
        return Http404

    try:
        client = Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        return Http404

    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
    elif request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def client_operations_list(request, client_id):
    try:
        Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        return Http404
    if request.method == 'GET':
        operations = Operation.objects.filter(client__id=client_id)
        serializer = OperationSerializer(operations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(client_id=client_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def client_operations_detail(request, client_id, operation_id):
    try:
        Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        return Http404

    try:
        operation = Operation.objects.get(id=operation_id)
    except Operation.DoesNotExist:
        return Http404

    if request.method == 'GET':
        serializer = OperationSerializer(operation)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
    elif request.method == 'PUT':
        serializer = OperationSerializer(operation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        operation.delete()
        return Response(status=status.HTTP_200_OK)
