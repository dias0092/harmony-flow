# Generated by Django 4.2.3 on 2023-07-28 06:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Artist",
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
                ("name", models.CharField(max_length=100)),
                ("genre", models.CharField(blank=True, max_length=100, null=True)),
                ("image", models.URLField(blank=True, null=True)),
            ],
        ),
    ]
