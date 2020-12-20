from django.test import TestCase
from app.forms.registration_form import UserForm


class FormTest(TestCase):

    def test_if_first_name_is_empty_should_return_False(self):
        form = UserForm(data={
            'username': 'Username',
            'first_name': '',
            'last_name': 'Last',
            'email': 'Email@abv.bg',
            'password1': 'kesten123',
            'password2': 'kesten123'
        })
        self.assertFalse(form.is_valid())

    def test_if_last_name_is_empty_should_return_False(self):
        form = UserForm(data={
            'username': 'Username',
            'first_name': 'First',
            'last_name': '',
            'email': 'Email@abv.bg',
            'password1': 'kesten123',
            'password2': 'kesten123'
        })
        self.assertFalse(form.is_valid())
