# Generated by Django 4.2.7 on 2023-11-21 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ModelTesting', '0009_pricing_services_pricing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='pricing',
        ),
        migrations.DeleteModel(
            name='Pricing',
        ),
    ]