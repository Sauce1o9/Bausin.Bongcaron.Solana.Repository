# Generated by Django 5.1.3 on 2024-11-30 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0018_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='checkout_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='checkout_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
