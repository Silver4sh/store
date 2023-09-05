from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.validators import MinValueValidator
from store_apps.inventory import  apps

class Inventory(models.Model):
    id_inventory = models.CharField(primary_key=True, max_length=100, editable=False)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank=False)
    type = models.CharField(max_length=1, choices=apps.TYPE_CHOICES, default="0")
    cost = models.DecimalField(max_digits=100, decimal_places=2, validators=[MinValueValidator(0)], blank=False)
    desc = models.CharField(max_length=100000, blank=True, null=True)
    date_add = models.DateField(editable=False, default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id_inventory:
            get_type = self.type
            if get_type in apps.CODE_ITEM:
                self.id_inventory = get_type + str(apps.CODE_ITEM[get_type])
                apps.CODE_ITEM[get_type] += 1
        super().save(*args, **kwargs)

class InventoryIn(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(null=False, default=0)
    detein = models.DateField(editable=False, default=timezone.now)
    sequence = models.PositiveIntegerField(null=False, editable=False)

    def save(self, *args, **kwargs):
        last_squence = self.sequence or 0
        
        super().save(*args, **kwargs)

class InventoryOut(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(null=False, default=0)
    dateout = models.DateField(editable=False, default=timezone.now)
    sequence = models.PositiveIntegerField(null=False, default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class InventoryStock(models.Model):
    inventory = models.OneToOneField(Inventory, on_delete=models.CASCADE, primary_key=True)
    qty = models.PositiveIntegerField(null=False, editable=True)

@receiver(post_save, sender=Inventory)
def create_inventory_stock(sender, instance, created, **kwargs):
    if created:
        InventoryStock.objects.create(inventory=instance, qty=0)

@receiver(post_save, sender=InventoryIn)
@receiver(post_save, sender=InventoryOut)
def update_inventory_stock(sender, instance, **kwargs):
    inventory = instance.inventory
    stock = InventoryStock.objects.get(inventory=inventory)
    total_in = InventoryIn.objects.filter(inventory=inventory).aggregate(models.Sum('qty'))['qty__sum'] or 0
    total_out = InventoryOut.objects.filter(inventory=inventory).aggregate(models.Sum('qty'))['qty__sum'] or 0
    #stock, created = InventoryStock.objects.get_or_create(inventory=inventory)

    if stock.qty >= total_out:
        stock.qty = total_in - total_out
        stock.save()
    else:
        # Handle the case where stock in is less than stock out
        raise Exception("Stock In cannot be less than Stock Out")