from rest_framework import serializers
from shop_system.models import *
from shop_system.finance_operations import *
from shop_system.observer import *


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('id', 'type', 'name', 'time',)


class ClientSerializer(serializers.ModelSerializer):
    rate_name = serializers.SerializerMethodField('generate_rate_name', read_only=True)
    rate_id = serializers.IntegerField(write_only=True)

    @staticmethod
    def generate_rate_name(self):
        return self.rate.type + ' ' + self.rate.name

    def create(self, validated_data):
        rate = Rate.objects.get(id=validated_data["rate_id"])
        validated_data["rate"] = rate
        account = Account.objects.get(id=validated_data["account_id"])
        validated_data["account"] = account
        validated_data["open_date"] = datetime.date.today()
        client = Client.objects.create(**validated_data)
        return client

    class Meta:
        model = Client
        fields = ('id', 'last_name', 'first_name', 'email', 'currency', 'dni', 'phone', 'address', 'credit_total', 'compensatory_value',
                  'moratorium_value', 'quotation', 'open_date', 'maintenance', 'rate_name', 'rate_id')


class OperationSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField('calculate_total', read_only=True)
    future = serializers.SerializerMethodField('calculate_future_call', read_only=True)

    @staticmethod
    def calculate_future_call(self):
        s = fo.calculate_operation_future(self)
        return s

    @staticmethod
    def calculate_total(self):
        c = fo.calculate_total(self)
        return c

    def create(self, validated_data):
        client = Client.objects.get(id=validated_data["client_id"])
        validated_data["client"] = client
        validated_data["operation_date"] = datetime.date.today()
        operation = Operation.objects.create(**validated_data)
        maintenance_date_verify(operation)
        return operation

    def update(self, instance, validated_data):
        instance.state = validated_data.get('state', instance.state)
        instance.payed = validated_data.get('payed', instance.payed)
        if instance.state or instance.payed != 0:
            instance.pay_date = datetime.date.today()
            t = calculate_operation_future(instance)
            instance.balance = t - instance.payed
        instance.save()
        return instance

    class Meta:
        model = Operation
        fields = ('id', 'operation_date', 'state', 'delivery', 'future', 'time', 'balance', 'total',
                  'maintenance', 'pay_date', 'payed',)


class ProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        account = Account.objects.get(id=validated_data["account_id"])
        validated_data["account"] = account
        product = Product.objects.create(**validated_data)
        return product

    class Meta:
        model = Product
        fields = ('id', 'name', 'unit_cost', 'measurement')


class OperationProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    unit_cost = serializers.FloatField(source='product.unit_cost', read_only=True)
    measurement = serializers.CharField(source='product.measurement', read_only=True)
    total = serializers.SerializerMethodField('calculate_total', read_only=True)

    @staticmethod
    def calculate_total(self):
        if isinstance(self, str):
            return self
        else:
            total = self.product.unit_cost * self.quantity
            return total

    def create(self, validated_data):
        operation = Operation.objects.get(id=validated_data["operation_id"])
        product = Product.objects.get(id=validated_data["product_id"])
        validated_data["product"] = product
        validated_data["operation"] = operation
        operation_product = OperationProduct.objects.create(**validated_data)
        response = credit_validator(operation_product, operation)
        if isinstance(response, str):
            return response
        return operation_product

    class Meta:
        model = OperationProduct
        fields = ('id', 'product_name', 'unit_cost', 'quantity', 'measurement', 'total')
