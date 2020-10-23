from django.urls import path

from user_system.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', users_list, name='user_list'),
    path('users/<int:user_id>/', users_detail, name='user_detail'),
    path('accounts/', accounts_list, name='account_list'),
    path('accounts/<int:account_id>', account_detail, name='account_detail'),
]