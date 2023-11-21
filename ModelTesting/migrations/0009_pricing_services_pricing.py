# Generated by Django 4.2.7 on 2023-11-21 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ModelTesting', '0008_alter_services_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=1, default=0.0, max_digits=4)),
            ],
        ),
        migrations.AddField(
            model_name='services',
            name='pricing',
            field=models.OneToOneField(default=0.0, on_delete=django.db.models.deletion.CASCADE, to='ModelTesting.pricing'),
        ),
    ]
