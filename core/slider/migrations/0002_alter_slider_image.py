# Generated by Django 4.2.7 on 2024-12-08 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("slider", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="slider",
            name="image",
            field=models.ImageField(upload_to="uploads/slider/"),
        ),
    ]
