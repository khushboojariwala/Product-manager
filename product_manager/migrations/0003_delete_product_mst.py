# Generated by Django 5.0.1 on 2024-01-20 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_manager', '0002_product_manager_register'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product_mst',
        ),
    ]