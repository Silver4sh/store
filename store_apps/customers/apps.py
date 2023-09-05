from django.apps import AppConfig

GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("N", "Don't Choose"))

class CustomersAppsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customers'
