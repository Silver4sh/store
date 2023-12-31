# Generated by Django 4.2.2 on 2023-09-02 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_apps', '0056_alter_inventoryin_qty_alter_inventoryout_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryin',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='inventoryout',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='inventoryin',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_apps.inventory'),
        ),
        migrations.AlterField(
            model_name='inventoryin',
            name='qty',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='inventoryout',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_apps.inventory'),
        ),
        migrations.AlterField(
            model_name='inventoryout',
            name='qty',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
