from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from shop_system.serializers import *
from shop_system.observer import *


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
        bills_generator(clients)
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
def client_bills_list(request, client_id):
    try:
        Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        return Http404
    if request.method == 'GET':
        bills = Bill.objects.filter(client__id=client_id)
        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(client_id=client_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def client_bills_detail(request, client_id, bill_id):
    try:
        Client.objects.get(id=client_id)
    except Client.DoesNotExist:
        return Http404

    try:
        bill = Bill.objects.get(id=bill_id)
    except Bill.DoesNotExist:
        return Http404

    if request.method == 'GET':
        serializer = BillSerializer(bill)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
    elif request.method == 'PUT':
        serializer = BillSerializer(bill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        bill.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def bill_operations_list(request, bill_id):
    try:
        Bill.objects.get(id=bill_id)
    except Bill.DoesNotExist:
        return Http404
    if request.method == 'GET':
        operations = Operation.objects.filter(bill__id=bill_id)
        serializer = OperationSerializer(operations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(bill_id=bill_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def bill_operations_detail(request, bill_id, operation_id):
    try:
        Bill.objects.get(id=bill_id)
    except Bill.DoesNotExist:
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
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        operation.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def operation_products_create(request, operation_id, product_id):
    try:
        Operation.objects.get(id=operation_id)
    except Operation.DoesNotExist:
        return Http404
    try:
        Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Http404

    if request.method == 'POST':
        serializer = OperationProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(operation_id=operation_id, product_id=product_id)
            if not isinstance(serializer.data["total"], str):
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def operation_products_list(request, operation_id, ):
    try:
        Operation.objects.get(id=operation_id)
    except Operation.DoesNotExist:
        return Http404
    if request.method == 'GET':
        operation_products = OperationProduct.objects.filter(operation__id=operation_id)
        serializer = OperationProductSerializer(operation_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def operation_products_detail(request, operation_product_id):
    try:
        operation_product = OperationProduct.objects.get(id=operation_product_id)
    except OperationProduct.DoesNotExist:
        return Http404

    if request.method == 'PUT':
        serializer = OperationProductSerializer(operation_product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer = OperationProductSerializer(operation_product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        operation_product.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def products_list(request, account_id):
    try:
        Account.objects.get(id=account_id)
    except Account.DoesNotExist:
        return Http404

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(account_id=account_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        products = Product.objects.filter(account__id=account_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def products_detail(request, account_id, product_id):
    try:
        Account.objects.get(id=account_id)
    except Account.DoesNotExist:
        return Http404
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Http404

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_200_OK)
