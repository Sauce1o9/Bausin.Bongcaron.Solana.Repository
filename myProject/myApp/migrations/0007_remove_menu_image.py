# Generated by Django 5.1.3 on 2024-11-19 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_menu_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='image',
        ),
    ]
