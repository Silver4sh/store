# Generated by Django 4.2.2 on 2023-06-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_apps', '0024_alter_customer_last_name_alter_customer_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='middle_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]