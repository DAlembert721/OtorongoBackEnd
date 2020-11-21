from django.urls import path, include

from shop_system.views import *

urlpatterns = [
    path('rates/', rates_list, name="rate_list"),
    path('accounts/<int:account_id>/clients/', account_clients_list, name="client_list"),
    path('accounts/<int:account_id>/clients/<int:client_id>/', account_clients_detail, name="client_detail"),
    path('clients/<int:client_id>/operations/', client_operations_list, name="operation_list"),
    path('clients/<int:client_id>/operations/<int:operation_id>/', client_operations_detail, name="operation_detail"),
    path('clients/<int:client_id>/operations/date=<str:date>/', client_date_operations_detail, name="date_operation"),
    path('clients/<int:client_id>/operations/state=<str:state>/', client_state_operations_list,
         name="state_operations"),
    path('operations/<int:operation_id>/products/<int:product_id>/', operation_products_create,
         name="operation_products_post"),
    path('operations/<int:operation_id>/operations-products/', operation_products_list, name='operation_product_list'),
    path('operations-products/<int:operation_product_id>/', operation_products_detail, name="operation_product"),
    path('accounts/<int:account_id>/products/', products_list, name="products_list"),
    path('accounts/<int:account_id>/products/<int:product_id>/', products_detail, name="products_detail"),
]
