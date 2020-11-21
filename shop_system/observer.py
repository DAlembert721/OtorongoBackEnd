import shop_system.finance_operations as fo
import datetime

from shop_system.models import Operation


def maintenance_date_verify(operation):
    if operation.operation_date.day == operation.client.open_date.day:
        operation.maintenance = operation.client.maintenance
        operation.save()


def close_operations(client):
    operations = Operation.objects.filter(client__id=client.id)
    for operation in operations:
        operation.close = True
        operation.save()
