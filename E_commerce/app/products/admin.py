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

