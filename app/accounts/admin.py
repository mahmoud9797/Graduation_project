# apps/users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Fields to display in the list view
    list_display = ('email', 'username', 'first_name', 'last_name', 'phone', 'is_active', 'is_staff', 'created_at')
    
    # Fields to filter by in the list view
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'created_at')
    
    # Fields to search by in the list view
    search_fields = ('email', 'username', 'first_name', 'last_name', 'phone')
    
    # Default ordering of the list view
    ordering = ('-created_at',)
    
    # Fields to display in the user detail view
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone', 'address')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Fields to display when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
