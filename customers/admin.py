from django.contrib import admin
from .models import Customers


class CustomersAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]
    search_fields = ["name", "address", "remarks"]
    list_filter = (
        "name",
        "is_active",
        "is_deleted",
    )
    fieldsets = (
        ("Basic Information", {"fields": ("name", "address", "remarks")}),
        ("Other Information", {"fields": ("is_active", "is_deleted", "created_by")}),
    )

    list_display = (
        "id",
        "name",
        "address",
        "remarks",
        "is_active",
        "is_deleted",
        "created_by",
        "created_at",
        "updated_at",
    )
    # readonly_fields = ("created_by",)


admin.site.register(Customers, CustomersAdmin)
