from django.contrib import admin
from .models import Transactions, TransactionDetails, GameTimings
from django.contrib.admin.options import TabularInline


class TransactionDetailsAdminInline(TabularInline):
    extra = 1
    max_num = 1
    model = TransactionDetails


class GameTimingsAdminInline(TabularInline):
    extra = 1
    max_num = 1
    model = GameTimings


TEXT = "SOME TEXT CAN BE ADDED HERE"


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]
    search_fields = ["detail"]
    list_filter = (
        "transaction_types",
        "transaction",
        "payment_mode",
        "amount",
        "business",
        "customer",
        "is_active",
        "is_deleted",
    )
    fieldsets = (
        (
            "Details",
            {
                "fields": ("customer", "detail", "remarks"),
                "description": f"{TEXT}",
                "classes": ("collapse",),
            },
        ),
        (
            "Transaction Info",
            {
                "fields": (
                    "amount",
                    "transaction_types",
                    "transaction",
                    "payment_mode",
                ),
            },
        ),
    )

    list_display = (
        "id",
        "detail",
        "remarks",
        "transaction_types",
        "transaction",
        "payment_mode",
        "amount",
        "business",
        "customer",
        "is_active",
        "is_deleted",
        "created_by",
        "created_at",
        "updated_at",
    )
    inlines = (TransactionDetailsAdminInline, GameTimingsAdminInline)

    def extra_fields_by_market(self):
        extra_inline_model = ""
        if self.transaction_types.Gaming:
            extra_inline_model = GameTimingsAdminInline
        elif self.transaction_types.Online:
            extra_inline_model = TransactionDetailsAdminInline
        return extra_inline_model

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            # hide/show market-specific inlines based on market name
            if obj and obj.extra_fields_by_market() == inline.__class__.__name__:
                yield inline.get_formset(request, obj), inline
