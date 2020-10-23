from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user_system.models import User, Account


# Register your models here.


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Account)

