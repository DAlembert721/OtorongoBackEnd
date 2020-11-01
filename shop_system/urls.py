from django.urls import path, include

from shop_system.views import *

urlpatterns = [
    path('rates/', rates_list, name="rate_list"),
    path('accounts/<int:account_id>/clients/', account_clients_list, name="client_list"),
    path('accounts/<int:account_id>/clients/<int:client_id>/', account_clients_detail, name="client_detail"),
    path('clients/<int:client_id>/bills/', client_bills_list, name="bill_list"),
    path('clients/<int:client_id>/bills/<int:bills_id>/', client_bills_detail, name="bill_detail"),
    path('bills/<int:bill_id>/operations/', bill_operations_list, name="operation_list"),
    path('bills/<int:bill_id>/operations/<int:operation_id>/', bill_operations_detail, name="operation_detail"),
    path('operations/<int:operation_id>/products/<int:product_id>/', operation_products_list,
         name="operation_products"),
    path('accounts/<int:account_id>/products/', products_list, name="products_list"),
    path('accounts/<int:account_id>/products/<int:product_id>/', products_detail, name="products_detail"),
]
