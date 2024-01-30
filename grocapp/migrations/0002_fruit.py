# Generated by Django 5.0.1 on 2024-01-15 11:29

import shortuuidfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('price', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(default='', upload_to='fruitimage')),
                ('description', models.TextField(default='', max_length=200)),
                ('quantity', models.CharField(default='', max_length=200)),
                ('sku', shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Fruit',
            },
        ),
    ]