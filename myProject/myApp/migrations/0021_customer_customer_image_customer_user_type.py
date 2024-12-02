# Generated by Django 5.1.3 on 2024-12-01 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0020_alter_checkout_checkout_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_image',
            field=models.ImageField(blank=True, null=True, upload_to='menu_images/'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]