from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class detail_transactions(models.Model):
    id_transaction = models.CharField(primary_key=True, max_length=1000, null=False, editable=False, default="T")
    id_item = models.CharField(primary_key=True, max_length=1000, null=False,editable=False)
    quantity = models.PositiveIntegerField(null=False, editable=False)
    cost = models.DecimalField(max_digits=100,decimal_places=2, validators=[MinValueValidator(0)], blank=False, null=False)
    pay = models.DecimalField(max_digits=100,decimal_places=2, validators=[MinValueValidator(0)], blank=False, null=False, default=quantity * cost)