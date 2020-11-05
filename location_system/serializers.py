from rest_framework import serializers

from location_system.models import *


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'name',)


class ProvinceSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        region = Region.objects.get(id=validated_data["region_id"])
        validated_data["region"] = region
        province = Province.objects.create(**validated_data)
        return province

    class Meta:
        model = Province
        fields = ('id', 'name',)


class DistrictSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        province = Province.objects.get(id=validated_data["province_id"])
        validated_data["province"] = province
        district = District.objects.create(**validated_data)
        return district

    class Meta:
        model = District
        fields = ('id', 'name',)
