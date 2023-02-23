from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import RegistrationForm
from .models import *
from django.contrib.admin import AdminSite

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'middle_name',)}),
        ('Permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser',
                                    'groups', 'user_permissions',)}),
        ('Important dates', {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name','role','is_active','is_staff','password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name','last_name', 'is_staff', 'id','get_role')
    search_fields = ('email', 'first_name', 'id')
    list_display_links = ('id','email')
    ordering = (CustomUser.USERNAME_FIELD,)

    def get_role(self,obj):
        return obj.role
