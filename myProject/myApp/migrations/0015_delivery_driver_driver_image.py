# Generated by Django 5.1.3 on 2024-11-23 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0014_orders_delivery_address_orders_order_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery_driver',
            name='driver_image',
            field=models.ImageField(blank=True, null=True, upload_to='menu_images/'),
        ),
    ]