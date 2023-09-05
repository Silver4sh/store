from django.apps import AppConfig

GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("N", "Don't Choose"))
JOB_TITLE_CHOICES = (("A","!"),("B","2"))
PLACEMENT_CHOICES = (("1","1"),("2","2"),("3","3"))
ACTIVE_CHOICE = (("1", "Active"), ("0", "Non-Active"))


class EmployeesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'employees'