# Generated by Django 5.0.1 on 2024-01-21 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocapp', '0014_category_alter_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
    ]
