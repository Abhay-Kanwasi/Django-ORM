# Generated by Django 4.2.7 on 2023-11-18 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelTesting', '0006_alter_services_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='categories',
            field=models.ManyToManyField(to='ModelTesting.category'),
        ),
    ]