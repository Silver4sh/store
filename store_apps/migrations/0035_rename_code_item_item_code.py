# Generated by Django 4.2.2 on 2023-06-17 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_apps', '0034_alter_item_code_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='code_item',
            new_name='code',
        ),
    ]