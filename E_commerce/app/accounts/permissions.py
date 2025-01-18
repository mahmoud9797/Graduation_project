
# accounts/permissions.py
from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow:
    - Owners of an account to edit it
    - Admins to edit any account
    """
    
    def has_permission(self, request, view):
        # Allow authenticated users
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Admin permissions
        if request.user.is_staff:
            return True
            
        # Owner permissions
        return obj.id == request.user.id
