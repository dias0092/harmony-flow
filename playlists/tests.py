from django.test import TestCase
from django.urls import reverse
from datetime import timedelta
from .models import Playlist, PlaylistTrack, User, Track
from albums.models import Album
from artists.models import Artist

class PlaylistTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.artist = Artist.objects.create(name="Test Artist", genre="Classic")
        self.album = Album.objects.create(name="Test Album", artist=self.artist, release_date="2023-01-01")
        self.playlist = Playlist.objects.create(user=self.user, name="Test Playlist")
        self.track = Track.objects.create(name="Test Track", album=self.album, duration=timedelta(minutes=3))
        self.playlist_track = PlaylistTrack.objects.create(playlist=self.playlist, track=self.track, order=1)

    def test_playlist_list_view(self):
        response = self.client.get(reverse('playlists:playlist_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Playlist')
        self.assertTemplateUsed(response, 'playlists/playlist_list.html')

    def test_playlist_detail_view(self):
        response = self.client.get(reverse('playlists:playlist_detail', args=[self.playlist.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Playlist')
        self.assertTemplateUsed(response, 'playlists/playlist_detail.html')

    def test_playlist_new_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse('playlists:playlist_new'), {
            'name': 'New Playlist',
        })
        self.assertEqual(response.status_code, 200)

    def test_playlist_edit_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse('playlists:playlist_edit', args=[self.playlist.id]), {
            'name': 'Updated Playlist',
        })
        self.assertEqual(response.status_code, 200)

    def test_playlist_delete_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse('playlists:playlist_delete', args=[self.playlist.id]))
        self.assertEqual(response.status_code, 302)
