# Generated by Django 4.2.2 on 2023-06-17 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_apps', '0031_alter_item_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='id',
        ),
        migrations.AddField(
            model_name='item',
            name='code_item',
            field=models.CharField(default=1, editable=False, max_length=10, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('0', 'N/A'), ('A', 'Electronics'), ('B', 'Otomotif')], default='0', max_length=1),
        ),
    ]
