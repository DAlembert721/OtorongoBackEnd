from shop_system.models import Bill, Operation
import shop_system.finance_operations as  fo
import datetime


def bills_generator(clients):
    for client in clients:
        today = datetime.date.today()
        date = datetime.date(today.year, today.month, client.billing_closing.day)
        try:
            Bill.objects.get(date=date)
        except Bill.DoesNotExist:
            bill = Bill(client=client, date=date, total=client.maintenance)
            bill.save()
            continue
        continue
    return


def update_bill_total(operation, bill_id):
    future = operation['future']
    bill = Bill.objects.get(id=bill_id)
    bill.total += future
    bill.save()


def update_operation_mount(item, operation_id):
    operation = Operation.objects.get(id=operation_id)
    operation.mount += item.quantity * item.product.unit_cost
    operation.save()
    if operation.close:
        future = fo.calculate_operation_future(operation)
        bill = operation.bill
        bill.total += future
        bill.save()
