from django.contrib import admin
from django.contrib.auth.models import Group as GroupDjango
from .models import User, Group
from django.contrib.auth.admin import UserAdmin as UserAdminDjango

# Register your models here.


admin.site.register(Group)
admin.site.unregister(GroupDjango)


@admin.register(User)
class UserAdmin(UserAdminDjango):
    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        else:
            return super().get_queryset(request).filter(username=request.user.username)

    def get_object(self, request, obj, from_field=None):
        if request.user.is_superuser:
            return super().get_object(request, obj, from_field)
        else:
            if request.user.username == obj:
                return super().get_object(request, obj, from_field)
            return None

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_readonly_fields(request, obj)
        else:
            if obj is None:
                return []
            else:
                return ['username', 'email', 'groups', 'user_permissions', 'is_staff', 'is_active', 'date_joined',
                        'last_login', 'is_superuser']

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_fields(request, obj)
        else:
            if obj is None:
                return []
            else:
                return ['username', 'password', 'first_name', 'last_name']

