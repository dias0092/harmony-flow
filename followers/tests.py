from django.test import TestCase
from django.urls import reverse
from .models import Follower
from artists.models import Artist
from users.models import User


class FollowerViewsTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(username='TestUser1', password='password123')
        self.artist1 = Artist.objects.create(name='Test Artist 1')
        self.follower1 = Follower.objects.create(user=self.user1, artist=self.artist1)

    def test_follower_list_view(self):
        response = self.client.get(reverse('followers:follower_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'{self.user1.username} follows {self.artist1.name}')
    
    def test_follower_detail_view(self):
        response = self.client.get(reverse('followers:follower_detail', args=(self.follower1.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'{self.user1.username} follows {self.artist1.name}')
    
    def test_follower_new_view(self):
        response = self.client.get(reverse('followers:follower_new'))
        self.assertEqual(response.status_code, 200)

    def test_follower_edit_view(self):
        response = self.client.get(reverse('followers:follower_edit', args=(self.follower1.pk,)))
        self.assertEqual(response.status_code, 200)

    def test_follower_delete_view(self):
        response = self.client.get(reverse('followers:follower_delete', args=(self.follower1.pk,)))
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.follower1.delete()
        self.user1.delete()
        self.artist1.delete()