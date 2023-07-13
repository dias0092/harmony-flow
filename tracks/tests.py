from django.test import TestCase
from django.urls import reverse
from datetime import timedelta
from .models import Album, Track
from artists.models import Artist

class TrackTests(TestCase):
    
    def setUp(self):
        self.artist = Artist.objects.create(name="Test Artist", genre="Classic")
        self.album = Album.objects.create(name="Test Album", artist=self.artist, release_date="2023-01-01")
        self.track = Track.objects.create(name="Test Track", album=self.album, duration=timedelta(minutes=3))

    def test_track_list_view(self):
        response = self.client.get(reverse('tracks:track_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Track')
        self.assertTemplateUsed(response, 'tracks/track_list.html')

    def test_track_detail_view(self):
        response = self.client.get(reverse('tracks:track_detail', args=[self.track.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Track')
        self.assertTemplateUsed(response, 'tracks/track_detail.html')

    def test_track_new_view(self):
        response = self.client.get(reverse('tracks:track_new'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tracks/track_edit.html')

    def test_track_edit_view(self):
        response = self.client.get(reverse('tracks:track_edit', args=[self.track.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tracks/track_edit.html')

    def test_track_delete_view(self):
        response = self.client.get(reverse('tracks:track_delete', args=[self.track.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tracks/track_delete.html')

    def tearDown(self):
        self.album.delete()
        self.track.delete()