# Generated by Django 4.2.2 on 2023-06-17 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_apps', '0022_remove_customer_cust_no_customer_id_cust'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]