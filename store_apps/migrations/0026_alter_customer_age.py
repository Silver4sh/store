# Generated by Django 4.2.2 on 2023-06-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_apps', '0025_alter_customer_last_name_alter_customer_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]