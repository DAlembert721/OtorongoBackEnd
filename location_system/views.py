from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from location_system.models import *
from location_system.serializers import *


@api_view(['GET'])
def regions_list(request):
    if request.method == 'GET':
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def region_provinces_list(request, region_id):
    try:
        Region.objects.get(id=region_id)
    except Region.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        provinces = Province.objects.filter(region__id=region_id)
        serializer = ProvinceSerializer(provinces, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def province_districts_list(request, province_id):
    try:
        Province.objects.get(id=province_id)
    except Province.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        districts = District.objects.filter(province__id=province_id)
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
