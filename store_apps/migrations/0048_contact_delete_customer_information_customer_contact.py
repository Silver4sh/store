# Generated by Django 4.2.2 on 2023-08-11 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_apps', '0047_rename_contact_customer_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('phone', models.BigIntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='customer_information',
        ),
        migrations.AddField(
            model_name='customer',
            name='contact',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='store_apps.contact'),
        ),
    ]
