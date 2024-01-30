# Generated by Django 5.0.1 on 2024-01-21 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocapp', '0013_alter_product_category_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Vegetable', 'Vegetable'), ('Fruit', 'Fruit'), ('Beverages', 'Beverages'), ('Oil&masala', 'Oil&masala'), ('Snacks', 'Snacks'), ('Soap&detergent', 'Soap&detergent'), ('Egg&meat', 'Egg&meat')], default='', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='grocapp.category'),
        ),
    ]