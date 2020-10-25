from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from user_system.models import User, Account


class UserSerializer(serializers.ModelSerializer):
    @staticmethod
    def validate_password(value: str) -> str:
        return make_password(value)

    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class AccountSerializer(UserSerializer):
    class Meta:
        model = Account
        fields = UserSerializer.Meta.fields + ('first_name', 'last_name', 'dni', 'phone', 'address',)
        extra_kwargs = UserSerializer.Meta.extra_kwargs.copy()
