<<<<<<< HEAD
# Generated by Django 5.1.4 on 2025-01-01 22:27
=======
# Generated by Django 5.1.4 on 2025-01-01 22:38
>>>>>>> origin/main

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(null=True)),
<<<<<<< HEAD
                ('price', models.DecimalField(decimal_places=2, max_digits=15, max_length=12)),
=======
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
>>>>>>> origin/main
                ('stock', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='products-images/')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.categories')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-created_at'],
            },
        ),
    ]
