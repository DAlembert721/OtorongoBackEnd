from shop_system.models import Bill
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
