# Generated by Django 5.1.1 on 2024-10-18 05:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_rename_flavor_product_flavour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flavour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flavours', to='dashboard.flavour'),
        ),
    ]
