# Generated by Django 4.2.2 on 2023-06-17 11:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store_apps', '0013_alter_customer_age_alter_customer_id_cust'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id_cust',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
