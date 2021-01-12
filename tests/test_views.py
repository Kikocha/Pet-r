from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from app.models.Pet import Pet


class HomePageViewTests(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_getHome_if_the_rightTemplates_are_used(self):
        response = self.test_client.get(reverse('home page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_page.html')
        context = response.context['Pets']
        self.assertIsNotNone(context)

    def test_getHome_if_a_pet_type_is_passed(self):
        response = self.test_client.get(reverse('pets filter', args=['other']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_page.html')

    def test_getRegister_if_the_rightTemplate_is_used(self):
        response = self.test_client.get(reverse('register page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration_and_login/register.html')

    def test_postRegister_if_the_rightRegisterForm_is_used_and_redirects(self):
        response = self.test_client.post(reverse('register page'), {
            'username': 'Username',
            'first_name': 'FirstName',
            'last_name': 'LastName',
            'email': 'Email@abv.bg',
            'password1': 'Passworddd',
            'password2': 'Passworddd',
            'phone_number': '0899238789',
        })
        self.assertEqual(response.status_code, 302)

    def test_getLogin_if_the_rightTemplate_is_used(self):
        response = self.test_client.get(reverse('login page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration_and_login/login.html')

    def test_postLogin_if_the_rightLoginForm_is_used_and_user_exists(self):
        response = self.test_client.post(reverse('login page'), {
            'username': 'Username',
            'password': 'Password',
        })
        self.assertEqual(response.status_code, 200)

    def test_getUserPosts_if_the_rightTemplate_is_used(self):
        response = self.test_client.get(reverse('my posts page', args=['Username']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_posts_page.html')

    def test_getAddPost(self):
        response = self.test_client.get(reverse('add post page'))
        self.assertEqual(response.status_code, 302)

    def test_postAddPost(self):
        response = self.test_client.post(reverse('add post page'), {
            'image': 'http://127.0.0.1:8000/media/pets/ferret.jpg',
            'months': '30',
            'type': 'other',
            'breed': 'Unknown',
            'gender': 'male',
            'description': 'Description',
            'location': 'Sofia',
            'user': 'user'
        })
        self.assertEqual(response.status_code, 302)
