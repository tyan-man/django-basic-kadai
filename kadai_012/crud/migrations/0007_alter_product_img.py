# Generated by Django 5.1.3 on 2024-11-10 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crud", "0006_alter_product_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="img",
            field=models.ImageField(default="images/noImage.png", upload_to="images/"),
        ),
    ]
