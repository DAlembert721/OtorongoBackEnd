from django.urls import path, include

from shop_system.views import *

urlpatterns = [
    path('rates/', rates_list, name="rate_list")
]