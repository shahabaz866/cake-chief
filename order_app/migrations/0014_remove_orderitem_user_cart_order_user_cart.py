# Generated by Django 5.1.1 on 2025-01-20 08:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0015_coupon_cart_coupon'),
        ('order_app', '0013_orderitem_user_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='user_cart',
        ),
        migrations.AddField(
            model_name='order',
            name='user_cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart_app.cart'),
        ),
    ]
