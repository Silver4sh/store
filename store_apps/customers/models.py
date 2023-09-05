from django.db import models
from django.utils import timezone
from store_apps.customers.assets import asset

QUEUE = 0

# Create your models here.
class cus_info(models.Model):
    email = models.EmailField(unique=True, blank=True)
    phone = models.BigIntegerField(blank=True, null=True)
    address = models.CharField(max_length=100)
    birthday = models.DateField(null=False)
    age = models.PositiveIntegerField(blank=True, null=True, editable=True)

    def save(self, *args, **kwargs):
        if self.birthday:
            today = timezone.now()
            self.age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        else:
            self.age = 0
        super().save(*args, **kwargs)

class customer(models.Model):
    QUEUE += 1

    id_cust = models.CharField(primary_key=True, max_length=100, editable=False, default="C" + str(QUEUE))
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, default="", blank=True)
    last_name = models.CharField(max_length=50, default="", blank=True)
    gender = models.CharField(max_length=1, choices=asset.GENDER_CHOICES, default="N")
    contact = models.OneToOneField(cus_info, on_delete=models.CASCADE, null=True)
    date_join = models.DateField(editable=False, default=timezone.now)
    edit_date = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)