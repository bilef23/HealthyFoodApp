# Generated by Django 4.2.13 on 2024-06-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthyFoodApp', '0002_product_price_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]