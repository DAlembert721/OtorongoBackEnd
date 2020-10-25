from rest_framework import serializers
from shop_system.models import *
from .finance_operations import *


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


class ProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        account = Account.objects.get(id=validated_data["account_id"])
        validated_data["account"] = account
        product = Product.objects.create(**validated_data)
        return product

    class Meta:
        model = Product
        fields = ('name', 'unit_cost')


class OperationProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    total = serializers.SerializerMethodField('calculate_total', read_only=True)

    @staticmethod
    def calculate_total(self):
        total = self.product.unit_cost * self.quantity
        return total

    def create(self, validated_data):
        product = Product.objects.get(id=validated_data["product_id"])
        operation = Operation.objects.get(id=validated_data["operation_id"])
        validated_data["product"] = product
        validated_data["operation"] = operation
        operation_product = OperationProduct.objects.create(**validated_data)
        return operation_product

    class Meta:
        model = OperationProduct
        fields = ('product_name', 'quantity', 'total',)
