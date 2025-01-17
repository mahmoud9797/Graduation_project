from django.contrib import admin
from .models import Categories, Products

# Register your models here.

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_at", "updated_at")

    fieldsets = ((None, {"fields":("name", "slug", "description", "image")}),
                 ("Timestamps",{"fields":("created_at", "updated_at"),
                                "classes":("collapse")
                                })
                 
                 )
    
    @admin.register(Products)
    class ProductAdmin(admin.ModelAdmin):
        list_display = ("name", "slug", "category", "price", "stock", "is_active", "created_at")
        list_filter = ("is_active", "category", "created_at")
        search_fields = ("name", "description")
        prepopulated_fields = {"slug":("name",)}
        readonly_fields = ("created_at", "updated_at")
        list_editable = ("price", "stock", "is_active")

        fieldsets = ((None, {"fields":("name", "slug", "description")}),
                     ("product Detials",{"fields":("category", "price", "stock", "image", "is_active")}),
                     ("Timestamps",{"fields":("created_at", "updated_at")
                     ,"classes" : ("collapse",)
                     }),

                     )
