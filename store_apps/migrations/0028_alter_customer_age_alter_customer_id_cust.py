# Generated by Django 4.2.2 on 2023-06-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_apps', '0027_alter_customer_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id_cust',
            field=models.PositiveIntegerField(default=1, editable=False, primary_key=True, serialize=False),
        ),
    ]