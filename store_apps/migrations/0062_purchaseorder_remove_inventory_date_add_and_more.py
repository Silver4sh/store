# Generated by Django 4.2.4 on 2023-10-01 15:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store_apps', '0061_alter_inventoryin_sequence'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_received', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='date_add',
        ),
        migrations.RemoveField(
            model_name='inventoryin',
            name='detein',
        ),
        migrations.RemoveField(
            model_name='inventoryout',
            name='dateout',
        ),
        migrations.AddField(
            model_name='inventory',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='inventoryin',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='inventoryin',
            name='source',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='inventoryout',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='inventoryout',
            name='destination',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='inventorystock',
            name='low_stock_threshold',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventoryin',
            name='sequence',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='inventoryout',
            name='sequence',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='inventorystock',
            name='qty',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='PurchaseOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty_ordered', models.PositiveIntegerField(default=0)),
                ('qty_received', models.PositiveIntegerField(default=0)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_apps.inventory')),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_apps.purchaseorder')),
            ],
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='items',
            field=models.ManyToManyField(through='store_apps.PurchaseOrderItem', to='store_apps.inventory'),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_apps.suplier'),
        ),
    ]
