from django.shortcuts import render
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

