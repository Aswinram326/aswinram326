# Generated by Django 5.0.1 on 2024-01-21 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocapp', '0015_rename_category_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='instock',
            field=models.BooleanField(default=True, null=True),
        ),
    ]