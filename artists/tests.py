from django.test import TestCase
from django.urls import reverse
from .models import Artist

class ArtistViewsCase(TestCase):

    def setUp(self):
        self.artist1 = Artist.objects.create(name='Test Artist 1')
        self.artist2 = Artist.objects.create(name='Test Artist 2')
    
    def test_artist_list_view(self):
        response = self.client.get(reverse('artists:artist_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Artist 1')
        self.assertContains(response, 'Test Artist 2')
    
    def test_artist_detail_view(self):
        response = self.client.get(reverse('artists:artist_detail', args=(self.artist1.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Artist 1')
    
    def test_artist_new_value(self):
        response = self.client.get(reverse('artists:artist_new'))
        self.assertEqual(response.status_code, 200)
    
    def test_artist_edit_view(self):
        response = self.client.get(reverse('artists:artist_edit', args=(self.artist1.pk,)))
        self.assertEqual(response.status_code, 200)
    
    def test_artist_delete_view(self):
        response = self.client.get(reverse('artists:artist_delete', args=(self.artist1.pk,)))
        self.assertEqual(response.status_code, 200)
    
    def test_artist_new_view_from_invalid(self):
        response = self.client.post(reverse('artists:artist_new'), {'name': ''}) 
        self.assertFormError(response, 'form', 'name', 'This field is required.')
    
    def tearDown(self):
        self.artist1.delete()
        self.artist2.delete()
