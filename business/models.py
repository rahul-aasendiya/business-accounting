from django.db import models
from django.contrib.auth.models import User
from customers.models import Customers


class Businesses(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=250)
    detail = models.TextField(null=True, blank=True)
    established_date = models.DateTimeField(blank=False, null=False)

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    customers = models.ManyToManyField(Customers)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="business_created_by"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "businesses"
        verbose_name_plural = "Business"
