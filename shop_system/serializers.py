from rest_framework import serializers
from shop_system.models import *
from shop_system.observer import *


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
        fields = ('id', 'last_name', 'first_name', 'dni', 'phone', 'address', 'credit_total', 'rate_value',
                  'quotation', 'billing_closing', 'payday', 'maintenance', 'rate_name', 'rate_id')


class BillSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField('calculate_future_call', read_only=True)
    balance = serializers.SerializerMethodField('calculate_payed', read_only=True)

    @staticmethod
    def calculate_future_call(self):
        s = fo.calculate_bill_future(self)
        return s

    @staticmethod
    def calculate_payed(self):
        s = fo.calculate_payed_mount(self)
        return s

    def create(self, validated_data):
        client = Client.objects.get(id=validated_data["client_id"])
        validated_data["client"] = client
        bill = Bill.objects.create(**validated_data)
        return bill

    class Meta:
        model = Bill
        fields = ('id', 'date', 'total', 'balance',)


class OperationSerializer(serializers.ModelSerializer):
    future = serializers.SerializerMethodField('calculate_future_call', read_only=True)

    @staticmethod
    def calculate_future_call(self):
        s = fo.calculate_operation_future(self)
        return s

    def create(self, validated_data):
        bill = Bill.objects.get(id=validated_data["bill_id"])
        validated_data["bill"] = bill
        operation = Operation.objects.create(**validated_data)
        return operation

    class Meta:
        model = Operation
        fields = ('operation_date', 'state', 'delivery', 'future', 'close')


class ProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        account = Account.objects.get(id=validated_data["account_id"])
        validated_data["account"] = account
        product = Product.objects.create(**validated_data)
        return product

    class Meta:
        model = Product
        fields = ('id', 'name', 'unit_cost')


class OperationProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    unit_cost = serializers.FloatField(source='product.unit_cost', read_only=True)
    total = serializers.SerializerMethodField('calculate_total', read_only=True)
    close = serializers.BooleanField(default=False, required=False, write_only=True)

    @staticmethod
    def calculate_total(self):
        total = self.product.unit_cost * self.quantity
        return total

    def create(self, validated_data):
        operation = Operation.objects.get(id=validated_data["operation_id"])
        if not operation.close:
            product = Product.objects.get(id=validated_data["product_id"])
            validated_data["product"] = product
            validated_data["operation"] = operation
            close = validated_data.pop('close')
            operation_product = OperationProduct.objects.create(**validated_data)
            operation.close = close
            operation.save()
            return operation_product
        else:
            return Exception

    class Meta:
        model = OperationProduct
        fields = ('id', 'product_name', 'unit_cost', 'quantity', 'total', 'close')
