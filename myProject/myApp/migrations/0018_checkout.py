# Generated by Django 5.1.3 on 2024-11-30 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0017_delete_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('checkout_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('checkout_description', models.CharField(max_length=100)),
                ('checkout_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('checkout_image', models.ImageField(blank=True, null=True, upload_to='menu_images/')),
                ('checkout_customer', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
