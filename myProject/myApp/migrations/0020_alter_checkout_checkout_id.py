# Generated by Django 5.1.3 on 2024-11-30 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0019_checkout_checkout_id_alter_checkout_checkout_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='checkout_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]