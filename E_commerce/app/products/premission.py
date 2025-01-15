from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    """
    Custom permission to allow only admin users to create products.
    """
    def has_permission(self, request, view):
        # Allow only users with `is_staff=True` to create products
        if request.method == 'POST':
            return request.user and request.user.is_staff
        return True  # Allow GET, PUT, etc., based on other permissions
