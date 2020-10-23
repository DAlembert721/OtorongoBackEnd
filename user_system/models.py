from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from location_system.models import District
from .managers import UserManager


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def _str_(self):
        return self.email

    class Meta:
        db_table = 'users'


class Account(User):
    accounts = models.OneToOneField(User, auto_created=True, on_delete=models.CASCADE, parent_link=True,
                                    primary_key=True, serialize=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dni = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=90)
    district = models.ForeignKey(District, null=True, on_delete=models.SET(None))

    class Meta:
        db_table = 'accounts'
