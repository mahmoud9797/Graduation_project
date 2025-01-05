from django.contrib import admin
from .models import Reviews

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("user", "product","rating" , "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("user__email", "product__name", "comment")
    readonly_fields = ("created_at", "updated_at")
    raw_id_fields = ("user", "product")

    fieldsets = ((None, {"fields": ("user", "product", "rating", "comment")}),
                 ("Timestamps",{"fields":("created_at", "updated_at")
                                , "classes" : ("collapse,")
                                })
                 
                 )
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=request.user)