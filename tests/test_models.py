from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.test import TestCase

from app.models.Pet import Pet


class PetTest(TestCase):
    def test_if_max_months_value_is_exceeded_should_return_error(self):
        with self.assertRaises(ValidationError) as context:
            user = User(username='Kikochai', password='kesten123')
            user.save()
            pet = Pet(image='http://127.0.0.1:8000/media/pets/ferret.jpg', months=201, type='Dog', breed='Pitbull',
                      gender='Male', description='description',
                      location='sofia', user=user)
            pet.full_clean()
            pet.save()
        self.assertIsNotNone(context.exception)

    def test_if_min_months_value_is_exceeded_should_return_error(self):
        with self.assertRaises(ValidationError) as context:
            user = User(username='Kikochai', password='kesten123')
            user.save()
            pet = Pet(image='http://127.0.0.1:8000/media/pets/ferret.jpg', months=-1, type='Dog', breed='Pitbull',
                      gender='Male', description='description',
                      location='sofia', user=user)
            pet.full_clean()
            pet.save()
        self.assertIsNotNone(context.exception)
