from django.db import models

QUEUE = 0

# Create your models here.

class suplier(models.Model):
    QUEUE += 1
    id_suplier = models.CharField(primary_key=True, max_length=100, editable=False, default="S" + str(QUEUE))
    company = models.CharField(max_length=100, blank=False)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(unique=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)