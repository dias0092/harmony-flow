from django.test import TestCase
from django.urls import reverse
from .models import Album, Artist
from datetime import date


class AlbumViewsTestCase(TestCase):

    def setUp(self):
        self.artist1 = Artist.objects.create(name='Test Artist 1')
        self.album1 = Album.objects.create(name='Test Album 1', artist=self.artist1, release_date=date.today())
        self.album2 = Album.objects.create(name='Test Album 2', artist=self.artist1, release_date=date.today())
    
    def test_album_list_view(self):
        response = self.client.get(reverse('albums:album_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Album 1')
        self.assertContains(response, 'Test Album 2')
    
    def test_album_detail_view(self):
        response = self.client.get(reverse('albums:album_detail', args=(self.album1.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Album 1')
        self.assertContains(response, 'Test Artist 1')
    
    def test_album_new_view(self):
        response = self.client.get(reverse('albums:album_new'))
        self.assertEqual(response.status_code, 200)
    
    def test_album_edit_view(self):
        response = self.client.get(reverse('albums:album_edit', args=(self.album1.pk,)))
        self.assertEqual(response.status_code, 200)

    def test_album_delete_view(self):
        response = self.client.get(reverse('albums:album_delete', args=(self.album1.pk,)))
        self.assertEqual(response.status_code, 200)
    
    def test_album_new_view_form_invalid(self):
        response = self.client.post(reverse('albums:album_new'), {'name': ''})  # missing name
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'name', 'This field is required.')

    def tearDown(self):
        self.album1.delete()
        self.album2.delete()
