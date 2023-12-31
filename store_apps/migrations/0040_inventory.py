# Generated by Django 4.2.4 on 2023-08-09 12:02

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store_apps', '0039_delete_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('code', models.CharField(editable=False, max_length=10000, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('0', 'N/A'), ('A', 'A'), ('B', 'B'), ('C', 'C')], default='0', max_length=1)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=100, validators=[django.core.validators.MinValueValidator(0)])),
                ('desc', models.CharField(blank=True, max_length=100000, null=True)),
                ('date_add', models.DateField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]
