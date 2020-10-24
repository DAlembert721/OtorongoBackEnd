from django.urls import path, include

from shop_system.views import *

urlpatterns = [
    path('rates/', rates_list, name="rate_list"),
    path('accounts/<int:account_id>/clients/', account_clients_list, name="client_list"),
    path('accounts/<int:account_id>/clients/<int:client_id>/', account_clients_detail, name="client_detail"),
    path('clients/<int:client_id>/operations/', client_operations_list, name="operation_list"),
    path('clients/<int:client_id>/operations/<int:operation_id>/', client_operations_detail, name="operation_detail"),

]