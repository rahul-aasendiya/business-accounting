from django.db import models
from django.contrib.auth.models import User


class Assets(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(blank=False, null=False, max_length=255)
    address = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="assets_created_by"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "assets"
        verbose_name_plural = "Assets"
