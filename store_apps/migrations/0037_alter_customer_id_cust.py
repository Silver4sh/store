# Generated by Django 4.2.4 on 2023-08-09 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_apps', '0036_alter_item_code_alter_item_cost_alter_item_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id_cust',
            field=models.PositiveIntegerField(default='C1', editable=False, primary_key=True, serialize=False),
        ),
    ]
