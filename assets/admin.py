from django.contrib import admin
from .models import Assets


class AssetsAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]
    search_fields = ["name", "address", "remarks"]
    list_filter = (
        "name",
        "is_active",
        "is_deleted",
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


admin.site.register(Assets, AssetsAdmin)
