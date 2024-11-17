# Generated by Django 4.2.7 on 2024-11-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Slider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="uploads/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
