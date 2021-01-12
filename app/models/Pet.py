from django.contrib.auth.models import User
from django.db import models

from app.models.validators import months_value_validator
PET_CHOICES = (
    ('Dog', 'dog'),
    ('Cat', 'cat'),
    ('Bird', 'bird'),
    ('Other', 'other'),

)

GENDER = (
    ('Female', 'female'),
    ('Male', 'male')
)


class Pet(models.Model):
    image = models.ImageField(upload_to='pets')
    months = models.IntegerField(blank=False, default=0, validators=[months_value_validator])
    type = models.CharField(choices=PET_CHOICES, blank=False, max_length=10)
    breed = models.CharField(default='Unknown', blank=False, max_length=20)
    gender = models.CharField(default='Male', blank=False, choices=GENDER, max_length=10)
    description = models.TextField(blank=False)
    location = models.CharField(default='Sofia', blank=False, max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
