# Generated by Django 5.1.1 on 2024-10-29 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_alter_product_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
