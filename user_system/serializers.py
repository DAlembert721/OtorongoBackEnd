from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from location_system.models import District
from user_system.models import User, Account


class UserSerializer(serializers.ModelSerializer):
    @staticmethod
    def validate_password(value: str) -> str:
        return make_password(value)

    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class AccountSerializer(UserSerializer):
    district_id = serializers.IntegerField(write_only=True)
    location = serializers.SerializerMethodField('location_name', read_only=True)

    @staticmethod
    def location_name(self):
        district = self.district.name
        province = self.district.province.name
        region = self.district.province.region.name
        return region + ',' + province + ',' + district

    def create(self, validated_data):
        district = District.objects.get(id=validated_data["district_id"])
        validated_data["district"] = district
        account = Account.objects.create(**validated_data)
        return account

    def update(self, instance, validated_data):
        instance.address = validated_data.get('address', instance.address)
        instance.organization = validated_data.get('organization', instance.organization)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

    class Meta:
        model = Account
        fields = UserSerializer.Meta.fields + ('first_name', 'last_name', 'dni', 'phone', 'address', 'organization'
                                               , 'ruc', 'district_id', 'location',)
        extra_kwargs = UserSerializer.Meta.extra_kwargs.copy()
