from django.contrib import admin
from .models import Businesses


class BusinessesAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]
    search_fields = ["name", "address", "established_date"]

    list_filter = (
        "name",
        "is_active",
        "is_deleted",
    )

    list_display = (
        "id",
        "name",
        "detail",
        "established_date",
        "is_active",
        "is_deleted",
        "created_by",
        "created_at",
        "updated_at",
    )


admin.site.register(Businesses, BusinessesAdmin)
