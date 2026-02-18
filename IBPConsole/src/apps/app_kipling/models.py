from django.db import models

class Products(models.Model):
    sku = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  # set once
    updated_at = models.DateTimeField(auto_now=True)      # auto update

    # class Meta:
    #     ordering = ["-created_at"]
    #     constraints = [
    #         models.CheckConstraint(
    #             check=models.Q(price__gte=0),
    #             name="price_non_negative",
    #         )
    #     ]

    def __str__(self):
        return f"{self.sku} - {self.name}"