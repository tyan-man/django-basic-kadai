# Generated by Django 5.1.3 on 2024-11-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crud", "0011_alter_product_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="img",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
    ]
