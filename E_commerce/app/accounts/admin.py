from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'is_active', 'is_staff', 'created_at')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'created_at')
    search_fields = ('email', 'username', 'first_name', 'last_name', 'phone')
    ordering = ['-created_at']

    fieldsets = (
        (None,{"fields":('email', 'username', 'password')}),
        ("personal info",{'fields':('first_name', 'last_name', 'phone', 'address')}),
        ('permissions', {'fields':("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("important dates",{"fields" : ("last_login", "created_at", "updated_at")}),
                 )
    

    readonly_fields = ("created_at", "updated_at")