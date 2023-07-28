# Generated by Django 4.2.3 on 2023-07-28 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("tracks", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserSong",
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
                ("play_date", models.DateTimeField(auto_now_add=True)),
                (
                    "song",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tracks.track"
                    ),
                ),
            ],
        ),
    ]
