import datetime
import shop_system.simple_rate_calculation as sr
import shop_system.compound_rate_calculation as cr
from shop_system.models import Operation, OperationProduct, Product


def calculate_operation_future(operation):
    products = OperationProduct.objects.filter(operation__id=operation.id)
    c = operation.delivery
    for product in products:
        item = Product.objects.get(id=product.product_id)
        unit_cost = item.unit_cost
        mount = product.quantity * unit_cost
        c += mount
    payday = operation.bill.date + datetime.timedelta(30)
    time = (payday - operation.operation_date).days
    if operation.bill.client.rate.type == 'Simple':
        rate = operation.bill.client.rate_value
        future = sr.calculo_futuro_a_tasa_simple(c, 0, time, rate, 'exacto')
        return future
    else:
        rate = [operation.bill.client.rate_value, operation.bill.client.rate.name]
        s = cr.futuro_a_tasa_compuesta(c, rate, time, operation.bill.client.quotation, operation.bill.client.rate.type)
        return s


def calculate_bill_future(bill):
    operations = Operation.objects.filter(bill__id=bill.id)
    future = 0
    for operation in operations:
        if not operation.state and operation.close:
            future += calculate_operation_future(operation)
    return future


def calculate_payed_mount(bill):
    operations = Operation.objects.filter(bill__id=bill.id)
    total = 0
    for operation in operations:
        if operation.state and operation.close:
            total += calculate_operation_future(operation)
    return total


def credit_validator(operation):
    total = calculate_bill_future(operation.bill)
    credit = operation.bill.client.credit_total
    if total > credit:
        operation.delete()
        return str(f'Credit line was exceeded by: {(total - credit)}')
    else:
        return None
