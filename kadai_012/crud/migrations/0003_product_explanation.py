# Generated by Django 5.1.3 on 2024-11-10 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_category_product_img_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='explanation',
            field=models.TextField(blank=True, null=True),
        ),
    ]
