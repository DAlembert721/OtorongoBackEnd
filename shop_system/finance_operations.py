import datetime
import shop_system.simple_rate_calculation as sr
import shop_system.compound_rate_calculation as cr
from shop_system.models import Operation, OperationProduct, Product


def calculate_operation_future(operation):
    if operation.balance != 0:
        c = operation.balance
    else:
        c = calculate_total(operation)

    today = datetime.date.today()
    time = (today - operation.operation_date).days
    days_past = time - operation.time
    future = 0
    if days_past > 0:
        if operation.client.rate.type == 'Simple':
            rate = operation.client.moratorium_value
            future = sr.calculo_futuro_a_tasa_simple(c, 0, days_past, rate, 'exacto')
        else:
            rate = [operation.client.moratorium_value, operation.client.rate.name]
            future = cr.futuro_a_tasa_compuesta(c, rate, days_past, operation.client.quotation,
                                                operation.client.rate.type)

    if operation.client.rate.type == 'Simple':
        rate = operation.client.compensatory_value
        future += sr.calculo_futuro_a_tasa_simple(c, 0, time, rate, 'exacto')

    else:
        rate = [operation.client.compensatory_value, operation.client.rate.name]
        future += cr.futuro_a_tasa_compuesta(c, rate, time, operation.client.quotation,
                                             operation.client.rate.type)
    return round(future, 2) + round(operation.maintenance, 2)


def credit_validator(operation_product, operation):
    operations = Operation.objects.filter(client__id=operation.client.id)
    total = 0
    for operation in operations:
        if not operation.state:
            total += calculate_operation_future(operation)
    credit = operation.client.credit_total
    if total > credit:
        operation_product.delete()
        return str(f'Credit line was exceeded by: {(total - credit)}')
    else:
        return None


def calculate_total(operation):
    products = OperationProduct.objects.filter(operation__id=operation.id)
    c = operation.delivery
    for product in products:
        item = Product.objects.get(id=product.product_id)
        unit_cost = item.unit_cost
        mount = round(product.quantity * unit_cost, 2)
        c += mount
    return c
