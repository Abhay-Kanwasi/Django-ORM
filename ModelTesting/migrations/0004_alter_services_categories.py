# Generated by Django 4.2.7 on 2023-11-16 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelTesting', '0003_alter_services_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='categories',
            field=models.ManyToManyField(related_query_name='services', to='ModelTesting.category'),
        ),
    ]
