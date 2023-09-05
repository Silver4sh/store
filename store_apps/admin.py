from django.contrib import admin
from .models import *

# Register your models here.

# Customers
admin.site.register(customer)
admin.site.register(cus_info)

# Employees
admin.site.register(employees)

# Inventory
admin.site.register(Inventory)
admin.site.register(InventoryIn)
admin.site.register(InventoryOut)
admin.site.register(InventoryStock)

# Suplier
admin.site.register(suplier)

