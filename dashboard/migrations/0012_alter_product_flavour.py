# Generated by Django 5.1.1 on 2024-10-25 04:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_product_dietary_info_product_is_bestseller_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flavour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='dashboard.flavour'),
        ),
    ]
