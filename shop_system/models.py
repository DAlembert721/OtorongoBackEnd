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
    credit_balance = models.FloatField(default=0)
    rate_value = models.FloatField()
    quotation = models.IntegerField(default=1)
    billing_closing = models.DateField()
    payday = models.DateField()
    maintenance = models.FloatField()
    rate = models.ForeignKey(Rate, null=True, on_delete=models.SET(None))

    class Meta:
        db_table = 'clients'


class Operation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    operation_date = models.DateField()
    state = models.BooleanField(default=0)
    delivery = models.FloatField()

    class Meta:
        db_table = 'operations'


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit_cost = models.FloatField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    operations = models.ManyToManyField(Operation, related_name='products')

    class Meta:
        db_table = 'products'
