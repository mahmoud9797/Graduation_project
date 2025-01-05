from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("created_at",)
    raw_id_fields = ('Products',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", 'total_amount', "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("user__email", 'user__username', "shipping_address")
    readonly_fields = ("created_at", "updated_at")
    inlines = [OrderItemInline]

    fieldsets = ((None,{"fields": ("user", "status", "total_amount")}),
                 ('shipping information',{"fields":("shipping_address",)}),
                 ("Timestamps",{"fields":("created_at", "updated_at"),
                                "classes": ("collapse",)
                                }),
                 
                 )


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=request.user)
