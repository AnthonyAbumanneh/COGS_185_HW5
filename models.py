from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import Q


class Item(models.Model):
    name = models.CharField(max_length=255)  # required by default
    serial_number = models.CharField(max_length=100, unique=True)  # required + unique
    quantity = models.IntegerField(validators=[MinValueValidator(0)])  # required, >= 0
    expiry_date = models.DateField()  # required
    created_at = models.DateTimeField(auto_now_add=True)  # auto timestamp
    notes = models.TextField(blank=True)  # optional

    class Meta:
        constraints = [
            # DB-level enforcement for quantity >= 0
            models.CheckConstraint(condition=Q(quantity__gte=0), name="quantity_gte_0"),
        ]

    def __str__(self):
        return f"{self.name} ({self.serial_number})"