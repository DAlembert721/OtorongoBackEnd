from rest_framework import serializers

from shop_system.models import *


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('id', 'type', 'name', 'time',)


class ClientSerializer(serializers.ModelSerializer):
    rate_name = serializers.CharField(source='rate.name', read_only=True)
    rate_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        rate = Rate.objects.get(id=validated_data["rate_id"])
        validated_data["rate"] = rate
        account = Account.objects.get(id=validated_data["account_id"])
        validated_data["account"] = account
        client = Client.objects.create(**validated_data)
        return client

    class Meta:
        model = Client
        fields = ('last_name', 'first_name', 'dni', 'phone', 'address', 'credit_total', 'credit_balance', 'rate_value',
                  'quotation', 'billing_closing', 'payday', 'maintenance', 'rate_name', 'rate_id')


class OperationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        client = Client.objects.get(id=validated_data["client_id"])
        validated_data["client"] = client
        operation = Operation.objects.create(**validated_data)
        return operation

    class Meta:
        model = Operation
        fields = ('operation_date', 'state', 'delivery',)


class Product(serializers.ModelSerializer):
    def create(self, validated_data):
        account = Account.objects.get(id=validated_data["account_id"])
        validated_data["account"] = account
        product = Product.objects.create(**validated_data)
        return product

    class Meta:
        model = Product
        fields = ('name', 'unit_cost')
