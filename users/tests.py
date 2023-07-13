from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class UserTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_user_list_view(self):
        response = self.client.get(reverse('users:user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_list.html')

    def test_user_detail_view(self):
        response = self.client.get(reverse('users:user_detail', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_detail.html')

    def test_user_new_view(self):
        response = self.client.get(reverse('users:user_new'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_edit.html')

    def test_user_edit_view(self):
        response = self.client.get(reverse('users:user_edit', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_edit.html')

    def test_user_delete_view(self):
        response = self.client.get(reverse('users:user_delete', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_delete.html')

    def test_register_view(self):
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_login_view(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302) 
