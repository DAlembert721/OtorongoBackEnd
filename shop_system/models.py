from django.db import models

# Create your models here.

from user_system.models import Account


class Rate(models.Model):
    name = models.CharField(max_length=20)
    time = models.IntegerField()
    type = models.CharField(max_length=10)

    class Meta:
        db_table = 'rates'


class Client(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    dni = models.CharField(max_length=11)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=90)
    credit_total = models.FloatField(default=0)
    compensatory_value = models.FloatField()
    moratorium_value = models.FloatField(default=0)
    quotation = models.IntegerField(default=1)
    open_date = models.DateField(null=True)
    maintenance = models.FloatField()
    rate = models.ForeignKey(Rate, null=True, on_delete=models.SET(None))

    class Meta:
        db_table = 'clients'


class Operation(models.Model):
    operation_date = models.DateField(null=True)
    state = models.BooleanField(default=False)
    delivery = models.FloatField(default=0)
    maintenance = models.FloatField(default=0)
    balance = models.FloatField(default=0)
    pay_date = models.DateField(null=True)
    time = models.IntegerField(default=30)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'operations'


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit_cost = models.FloatField()
    measurement = models.CharField(max_length=10)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    operations = models.ManyToManyField(Operation, related_name='products', through='OperationProduct',
                                        symmetrical=False)

    class Meta:
        db_table = 'products'


class OperationProduct(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE, related_name='operation_id')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_id')
    quantity = models.FloatField(default=0)

    class Meta:
        db_table = 'operations_products'
