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
            bill = Bill(client=client, date=date)
            bill.save()
            continue
        continue
    return

