# Generated by Django 5.0.1 on 2024-01-21 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocapp', '0010_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
