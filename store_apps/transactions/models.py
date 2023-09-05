from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.
class transaction(models.Model):
    id_transaction = models.CharField(primary_key=True, max_length=1000, null=False, editable=False, default='T')
    id_employee = models.CharField(primary_key=True, max_length=100, choices='', editable=False, null=False)
    created_date = models.DateField(editable=False, null=False, default=timezone.now)
    quantity = models.PositiveIntegerField(null=False,editable=False,default=())
    total_cost = models.DecimalField(max_digits=100, decimal_places=2, validators=[MinValueValidator(0)], blank=False)
    total_disc = models.DecimalField(max_digits=100, decimal_places=2, validators=[MinValueValidator(0)], blank=False)