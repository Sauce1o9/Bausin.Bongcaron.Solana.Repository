# Generated by Django 5.1.3 on 2024-11-23 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0011_remove_orders_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
