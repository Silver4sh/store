from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.validators import MinValueValidator

from store_apps.inventory.assets import asset
from store_apps.supliers.models import  suplier

class Inventory(models.Model):
    id_inventory = models.CharField(primary_key=True, max_length=100, editable=False)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank=False)
    type = models.CharField(max_length=1, choices=asset.TYPE_CHOICES, default="0")
    cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], blank=False)
    desc = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(editable=False, default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id_inventory:
            self.id_inventory = f"{self.type}{Inventory.objects.count() + 1:03d}"
        super().save(*args, **kwargs)

class InventoryMovement(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(null=False, default=0)
    date = models.DateTimeField(editable=False, default=timezone.now)
    sequence = models.PositiveIntegerField(null=False, editable=False, default=0)

    class Meta:
        abstract = True

class InventoryIn(InventoryMovement):
    source = models.CharField(max_length=100, blank=True)
    date_in = models.DateTimeField(editable=False, default=timezone.now)

class InventoryOut(InventoryMovement):
    destination = models.CharField(max_length=100, blank=True)

class InventoryStock(models.Model):
    inventory = models.OneToOneField(Inventory, on_delete=models.CASCADE, primary_key=True)
    qty = models.PositiveIntegerField(null=False, editable=True, default=0)
    low_stock_threshold = models.PositiveIntegerField(null=False, default=10)

class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(suplier, on_delete=models.CASCADE)
    items = models.ManyToManyField(Inventory, through='PurchaseOrderItem')
    order_date = models.DateTimeField(default=timezone.now)
    is_received = models.BooleanField(default=False)

class PurchaseOrderItem(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    qty_ordered = models.PositiveIntegerField(null=False, default=0)
    qty_received = models.PositiveIntegerField(null=False, default=0)

@receiver(pre_save, sender=PurchaseOrderItem)
def update_inventory_on_purchase(sender, instance, **kwargs):
    inventory = instance.inventory
    inventory.qty += instance.qty_received
    inventory.save()

@receiver(post_save, sender=Inventory)
def create_inventory_stock(sender, instance, created, **kwargs):
    if created:
        InventoryStock.objects.create(inventory=instance, qty=0)

#@receiver(post_save, sender=InventoryMovement)
#def update_inventory_stock(sender, instance, **kwargs):
#    inventory = instance.inventory
#    stock, created = InventoryStock.objects.get_or_create(inventory=inventory)
#    total_in = InventoryIn.objects.filter(inventory=inventory).aggregate(models.Sum('qty'))['qty__sum'] or 0
#    total_out = InventoryOut.objects.filter(inventory=inventory).aggregate(models.Sum('qty'))['qty__sum'] or 0

#    if stock.qty >= total_out:
#        stock.qty = total_in - total_out
#        stock.save()
#    else:
#        raise Exception("Stock In cannot be less than Stock Out")

@receiver(post_save, sender=InventoryIn)
def update_inventory_on_stock_in(sender, instance, **kwargs):
    inventory = instance.inventory
    stock, created = InventoryStock.objects.get_or_create(inventory=inventory)
    stock.qty += instance.qty  # Increase stock with the quantity from the incoming inventory
    stock.save()