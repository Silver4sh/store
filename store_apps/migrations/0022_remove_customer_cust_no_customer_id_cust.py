# Generated by Django 4.2.2 on 2023-06-17 14:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store_apps', '0021_rename_cust_customer_cust_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='cust_no',
        ),
        migrations.AddField(
            model_name='customer',
            name='id_cust',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
