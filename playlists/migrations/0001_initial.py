# Generated by Django 4.2.3 on 2023-07-09 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playlists.playlist')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracks.track')),
            ],
        ),
    ]