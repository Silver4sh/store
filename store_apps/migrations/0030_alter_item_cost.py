# Generated by Django 4.2.2 on 2023-06-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_apps', '0029_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
