from django.db import models
from django.utils import timezone
from store_apps.employees import apps


QUEUE = 0
# Create your models here.
class employees(models.Model):
    QUEUE += 1

    id_emp = models.CharField(primary_key=True, max_length=100,editable=False, default="E" + str(QUEUE))
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, default="", blank=True)
    last_name = models.CharField(max_length=50, default="", blank=True)
    gender = models.CharField(max_length=1, choices=apps.GENDER_CHOICES, default="N")
    job_title = models.CharField(max_length=3, choices=apps.JOB_TITLE_CHOICES, null=False)
    placement = models.CharField(max_length=3, choices=apps.PLACEMENT_CHOICES, null=False)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, default="")
    birthday = models.DateField(null=False)
    age = models.PositiveIntegerField(blank=True, null=True, editable=True)
    is_active = models.CharField(max_length=1, choices=apps.ACTIVE_CHOICE, null=False)
    date_join = models.DateField(editable=False, default=timezone.now)
    edit_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"Created User : {self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if self.birthday:
            today = timezone.now()
            self.age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        else:
            self.age = 0
        super().save(*args, **kwargs)