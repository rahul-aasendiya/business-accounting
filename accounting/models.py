from django.db import models
from django.contrib.auth.models import User
from customers.models import Customers
from business.models import Businesses

TRANSACTION_TYPES_CHOICES = (
    ("Gaming", "Gaming"),
    ("Printing", "Printing"),
    ("Assets", "Assets"),
    ("Other", "Other"),
)
TRANSACTION_CHOICES = (("In", "In"), ("Out", "Out"))
PAYMENT_MODE_CHOICES = (("Cash", "Cash"), ("Online", "Online"))


class Transactions(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    detail = models.TextField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    # We choose Assets when we need to record the Assets and customer will be null
    # Need to add hint in form when we select transaction status
    transaction_types = models.CharField(
        max_length=50,
        choices=TRANSACTION_TYPES_CHOICES,
        help_text="Some hint for this field will reside here.", 
    )
    transaction = models.CharField(max_length=50, choices=TRANSACTION_CHOICES)
    payment_mode = models.CharField(max_length=50, choices=PAYMENT_MODE_CHOICES)
    amount = models.FloatField(blank=False, null=False, default=0.0)
    # balance = we will calculate this and show in list
    business = models.ForeignKey(
        Businesses,
        on_delete=models.SET_NULL,
        null=True,
        related_name="business",
    )
    customer = models.ForeignKey(
        Customers,
        on_delete=models.SET_NULL,
        null=True,
        related_name="customer",
    )
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="accounting_created_by",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.transaction_types}"

    class Meta:
        db_table = "transactions"
        verbose_name_plural = "Transactions"


# In this table we will store to payment information like from which medium of payment is received  # noqa: E501
class TransactionDetails(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    transaction_details = models.ForeignKey(
        Transactions,
        on_delete=models.SET_NULL,
        null=True,
        related_name="transaction_detail",
    )
    detail = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        db_table = "transaction_details"
        verbose_name_plural = "Transaction Details"


class GameTimings(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    transaction_timing = models.ForeignKey(
        Transactions,
        on_delete=models.SET_NULL,
        null=True,
        related_name="game_timing",
    )
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)
    # duration = we will calculate the duration based on start time and end time
    # remaining time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.start_time} to {self.end_time} Duration: calculate based on timing."
        )

    class Meta:
        db_table = "game_timings"
        verbose_name_plural = "Game Timings"
