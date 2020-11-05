from django.urls import path, include

from location_system.views import *

urlpatterns = [
    path('regions/', regions_list, name='region_list'),
    path('regions/<int:region_id>/provinces/', region_provinces_list, name='province_list'),
    path('provinces/<int:province_id>/districts/', province_districts_list, name='district_list'),
]