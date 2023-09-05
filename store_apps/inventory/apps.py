from django.apps import AppConfig

CODE_ITEM = {
    "0": 1,
    "A": 1,
    "B": 1,
}


TYPE_CHOICES = (
    ("0", "N/A"),
    ("A", "A"),
    ("B", "B"),
    ("C", "C")
    )

class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory'
